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

Keep three kinds of statement apart when adding material: source-derived recommendations, owner preferences, and context-dependent judgment. Note which is which.

## Left out on purpose

- Social media assets and carousels. Not needed for now. Add a section when they are.
- SVG illustration specification (shape language, test sheet, SVGO budget). Add it when a project is illustration-led.

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
