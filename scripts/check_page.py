#!/usr/bin/env python3
"""Open a URL at several widths, take screenshots and report common problems.

Setup (once):
  pip install playwright
  python -m playwright install chromium

Usage:
  python check_page.py http://localhost:4173 [--widths 360 768 1280 1920]
                       [--out shots] [--wait 800] [--path-label home]

For each width it saves a full-page and a viewport screenshot, then reports:
  - horizontal overflow
  - console errors and uncaught page errors
  - text under 12px
  - interactive elements under 44 by 44 px
  - buttons, links and form controls with no accessible name
  - images with no alt attribute

What this does and does not show: it shows the page is well-formed and what the
code does in headless Chromium. It does not show how the page feels on a real
phone. Fixed elements appear mid-page in full-page shots, so look at the
viewport shots for bottom navigation. Web fonts may not load in a sandbox.

Exit code is 1 when any finding is reported.
"""
import argparse
import json
import os
import sys

from playwright.sync_api import sync_playwright

PROBE = r"""
() => {
  const out = { tinyText: [], smallTargets: [], unnamed: [], noAlt: [], overflow: null };
  const de = document.documentElement;
  out.overflow = de.scrollWidth > de.clientWidth + 1
    ? { scrollWidth: de.scrollWidth, clientWidth: de.clientWidth } : null;

  const visible = (el) => {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none';
  };
  const label = (el) => {
    const tag = el.tagName.toLowerCase();
    const id = el.id ? '#' + el.id : '';
    const cls = (el.className && typeof el.className === 'string')
      ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '';
    const text = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 30);
    return tag + id + cls + (text ? ` "${text}"` : '');
  };

  // Text under 12px: check elements that own a non-empty text node.
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const n = walker.currentNode;
    if (!n.nodeValue.trim()) continue;
    const el = n.parentElement;
    if (!el || seen.has(el) || !visible(el)) continue;
    seen.add(el);
    const size = parseFloat(getComputedStyle(el).fontSize);
    if (size < 12) out.tinyText.push({ el: label(el), size });
  }

  // Interactive elements.
  const sel = 'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [role=link], [role=tab], [role=checkbox], [role=switch], [tabindex]:not([tabindex="-1"])';
  document.querySelectorAll(sel).forEach((el) => {
    if (!visible(el)) return;
    const r = el.getBoundingClientRect();
    // Inline links inside running text are exempt from the target size check.
    const inline = el.tagName === 'A' && getComputedStyle(el).display === 'inline';
    if (!inline && (r.width < 44 || r.height < 44)) {
      out.smallTargets.push({ el: label(el), w: Math.round(r.width), h: Math.round(r.height) });
    }
    const aria = el.getAttribute('aria-label');
    const labelledby = el.getAttribute('aria-labelledby');
    const title = el.getAttribute('title');
    const imgAlt = el.querySelector('img[alt]:not([alt=""])');
    const hasLabelEl = el.id && document.querySelector(`label[for="${CSS.escape(el.id)}"]`);
    const wrapped = el.closest('label');
    const text = (el.innerText || el.value || '').trim();
    const isInput = ['INPUT', 'SELECT', 'TEXTAREA'].includes(el.tagName);
    const named = aria || labelledby || title || imgAlt || hasLabelEl || wrapped || (!isInput && text);
    if (!named) out.unnamed.push(label(el));
  });

  document.querySelectorAll('img').forEach((img) => {
    if (!img.hasAttribute('alt') && visible(img)) {
      out.noAlt.push((img.getAttribute('src') || '').slice(0, 60));
    }
  });
  return out;
}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--widths", type=int, nargs="+", default=[360, 768, 1280, 1920])
    ap.add_argument("--out", default="shots")
    ap.add_argument("--wait", type=int, default=800, help="ms to wait after load")
    ap.add_argument("--path-label", default="page", help="prefix for screenshot names")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    findings = 0
    report = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for w in args.widths:
            ctx = browser.new_context(viewport={"width": w, "height": 900})
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m, errors=errors: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
            page.on("pageerror", lambda e, errors=errors: errors.append(f"pageerror: {e}"))
            page.goto(args.url, wait_until="networkidle")
            page.wait_for_timeout(args.wait)
            base = os.path.join(args.out, f"{args.path_label}-{w}")
            page.screenshot(path=base + "-full.png", full_page=True)
            page.screenshot(path=base + "-viewport.png")
            probe = page.evaluate(PROBE)
            probe["consoleErrors"] = errors
            report[w] = probe
            ctx.close()
        browser.close()

    for w, r in report.items():
        print(f"\n== {w}px ==")
        checks = [
            ("Horizontal overflow", [r["overflow"]] if r["overflow"] else []),
            ("Console and page errors", r["consoleErrors"]),
            ("Text under 12px", r["tinyText"]),
            ("Targets under 44x44", r["smallTargets"]),
            ("Controls with no accessible name", r["unnamed"]),
            ("Images with no alt attribute", r["noAlt"]),
        ]
        for name, items in checks:
            if not items:
                print(f"  ok    {name}")
                continue
            findings += len(items)
            print(f"  FOUND {name}: {len(items)}")
            for item in items[:8]:
                print(f"        {json.dumps(item) if not isinstance(item, str) else item}")
            if len(items) > 8:
                print(f"        ... {len(items) - 8} more")

    print(f"\nScreenshots in {args.out}/. Findings: {findings}")
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
