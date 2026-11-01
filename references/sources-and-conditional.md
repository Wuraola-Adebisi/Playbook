# Sources, provenance and conditional guidance

## Where each part came from

| Material | Origin | Where it lives |
|---|---|---|
| Interaction principles (metaphors, continuous input, interruptibility, continuity, gesture intent, frequency, touch precision, scrolling, implicit input, Fitts's law, playfulness) | "Invisible Details of Interaction Design" article, July 2023, from the working draft | `interaction-and-a11y.md` |
| Practical typography, hit area, motion, feedback, accessibility and performance guidance | "Web Interface Guidelines" (github.com/raunofreiberg/interfaces), from the working draft | `foundations.md`, `interaction-and-a11y.md` |
| Reference research workflow, Mobbin notes | Working draft | `process.md` |
| shadcn/ui and installed-primitive reuse | Working draft and playbook | `build-and-verify.md` |
| Stages, inspiration analysis, style identity, brief template, decision labels, status block, reference log | Studio playbook | `process.md`, `SKILL.md` |
| Token conventions, foundation rules, anti-generic checklist, motion ladder, accessibility and performance floors, writing rules, QA checklist | Studio playbook | `foundations.md`, `interaction-and-a11y.md`, `writing.md`, `build-and-verify.md` |
| Audit procedure, verification protocol, sandbox pitfalls, name-collision warning, handover commands | Added from working on a real repo audit | `build-and-verify.md`, `foundations.md` |
| Writing preferences, no co-author credit | Owner preferences | `writing.md` |
| Altitude, depth and range, outside judge, self-efficacy levers | "How to be more ambitious: A tutorial for humans with models", Felix Rieseberg, 13 October 2026. Rewritten with frontend examples, not copied | `ambition.md`, `SKILL.md` working agreement |
| Build with shadcn, match the Figma styling | Owner instruction | `figma-and-shadcn.md` |
| Animation review with Emil Kowalski's skill | Owner instruction. His skill is referenced, not copied. Names and install command from his site and public listings | `motion-review.md` |
| Turn a finished workflow into a reusable skill | Owner instruction | `capture-workflow.md` |
| `contrast.py`, `check_page.py` | Written to match what the skill already described. `contrast.py` tested against known ratios. `check_page.py` compiles but had no browser to run against when written | `scripts/` |

Keep three kinds of statement apart when adding material: source-derived recommendations, owner preferences, and context-dependent judgment. Note which is which.

## Left out on purpose

- Social media assets and carousels. Not needed for now. Add a section when they are.
- SVG illustration specification (shape language, test sheet, SVGO budget). Add it when a project is illustration-led.
- The speed kind of ambition from the Rieseberg article, and its business examples (the quarterly review deck, churn analysis). They do not map to interface work.
- The text of Emil Kowalski's skills. Install his skill instead of copying it.

## Mobbin

- Setup: https://mobbin.com/mcp
- Documentation: https://docs.mobbin.com/mcp
- Server repository: https://github.com/mobbin/mobbin-mcp-server
- Hosted endpoint noted in the supplied research: `https://api.mobbin.com/mcp` (Streamable HTTP with OAuth)

Never state that Mobbin was used unless the active environment confirms the connector. Without it, use references that can legitimately be viewed.

## Conditional guidance

Apply these only when the stack or feature calls for them.

- **Theme switching in Next.js.** `next-themes` can switch themes without a flash. Suppress transitions during the switch so they do not fire across the whole interface.
- **Authentication redirects.** Prefer server-side handling to avoid a visible client-side URL change.
- **Video autoplay on iOS.** Use `muted` and `playsinline`. Pause or unmount offscreen video.
- **SVG favicons.** Can adapt to light and dark with `prefers-color-scheme`.
- **Nested menus.** Account for pointer travel so a submenu does not close when the pointer crosses a small gap.
- **Menu opening events.** Opening on `mousedown` can feel immediate, but check it against keyboard behavior, click semantics and accessibility before using it.
- **Keyboard shortcuts.** Implement deletion shortcuts such as Cmd+Backspace only when they are expected, discoverable and safe.
- **Gradient text.** Make sure selected text stays readable.
- **Font rendering.** `-webkit-font-smoothing: antialiased` and `text-rendering: optimizeLegibility` are rendering choices, not universal fixes.
- **Smooth scrolling.** Use it for in-page navigation only when it helps, with a scroll offset for fixed headers.
- **Glow and blur effects.** Scaled or blurred filled rectangles can show banding. A radial gradient is often a better fit.
- **High-frequency values.** Direct DOM updates through refs can avoid excess React renders. Measure first and keep React in charge of structure.
- **Adaptive behavior.** Reduce expensive effects on constrained devices or networks when it improves the experience.
- **Browser and platform quirks.** Focus-ring details and platform gestures change. Check current support and test on the target platforms before relying on an old caveat.
