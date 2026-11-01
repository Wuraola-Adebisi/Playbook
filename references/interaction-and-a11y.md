# Interaction, states, accessibility and performance

Treat these as informed defaults. Context, task and platform decide.

## Interaction principles

- **Familiar metaphors.** Reuse patterns users can predict. A metaphor earns its place when it clarifies behavior.
- **Continuous input.** Where it fits, respond to a gesture as it happens instead of waiting for a threshold and jumping. Drag and scrub update the interface directly.
- **Interruptibility.** Motion shows momentum and direction, and never traps the user mid-transition.
- **Spatial continuity.** Show where something came from and where it went. Morphing helps only when it supports understanding.
- **Gesture intent.** A lightweight action may respond during a swipe. A destructive action waits until intent is clear, and is never easy to trigger by accident.
- **Frequency and novelty.** Frequent, low-novelty actions get minimal overhead. Expressive motion is for rare, meaningful moments.
- **Touch precision.** A finger hides what it manipulates. Offer persistent handles, previews or offset positioning for precise work, and size targets generously.
- **Scrolling and landmarks.** Never hijack scroll or route input to an unintended region. Long pages get landmarks: anchors, progress, back to top.
- **Implicit input.** Context can reduce effort. Inferred defaults must be visible, reversible and free of location or personal data unless the user chose it.
- **Fitts's law.** Important targets are large and near the thing they act on.
- **Playfulness.** Welcome where it costs nothing in clarity, accessibility or task completion. It is context-dependent, not a requirement.

## Flow and state inventory

Before building a flow, list its states: initial, loading, empty, success, error (with field-level causes), disabled, offline or storage unavailable, and any destructive step. Each state gets a design and its copy. Keep the inventory in the brief.

- **Empty states** offer the next useful action. A first run asks for the one or two facts the product needs and explains what they unlock.
- **No backend?** Use a small async data module with realistic latency and a switch that forces failures, so loading and error states are real.
- **Browser storage** is wrapped in try/catch and has a working empty state. Offer a way to export a backup when the data lives only on the device.
- **Optimistic updates** roll back with a clear message when the operation fails.

## Forms

- Every field has a visible label tied to it with `htmlFor`/`id` or by wrapping. Placeholder-only labels are not labels.
- Use a real `form` so Enter submits. Set input types, `inputMode`, `required` and `autocomplete`. Do not disable browser help for names, emails, addresses or authentication.
- Errors appear next to the field, name the field and say how to fix it. Link them with `aria-describedby` and set `aria-invalid`.
- Do not disable a submit button to signal invalid input. Show the errors.
- Block duplicate submits while a request is pending, and explain the pending state.
- Inputs are 16px or larger. Do not autofocus on touch devices. On pointer devices, focusing the first field in a dialog is a good default.
- Toggles take effect immediately when that matches their meaning.
- A disabled control is not explained by a tooltip, because disabled controls are often not focusable. Use visible helper text.

## Feedback and consequence

- Feedback appears near the action. A check beside a copy button beats a distant toast.
- Lightweight actions respond at once and offer undo. Removing an item restores it to its old position.
- Destructive or irreversible actions need confirmation, or a gesture that makes intent clear.
- Toasts that offer undo stay long enough to use (about seven seconds) and are announced to assistive technology (`role="status"`).

## Hit areas

- At least 44 by 44 px. A 24px icon still has a 44px target through padding or a transparent extension.
- Adjacent targets leave no dead gaps.
- Hover styles apply only where hover exists (`@media (hover: hover)`).
- Purely decorative overlays and glows use `pointer-events: none`.
- Do not disable text selection across a page. Disable it only on the inner text of a control when selecting it interferes.
- Remove the iOS tap highlight only where a visible pressed state replaces it.

## Accessibility floor

- WCAG 2.1 AA as the minimum.
- Visible keyboard focus on every interactive element. A 3px ring with an offset works on busy backgrounds. Never remove an outline without a replacement.
- Full keyboard operability, including sliders, maps and drag interactions. Drag always has a non-drag alternative.
- Semantic HTML first: landmarks, one `h1` per page, logical heading order, real buttons and links.
- Dialogs: prefer native `dialog` with `showModal()`, which provides focus trapping, Escape and an inert background. Label with `aria-labelledby`, restore focus to the trigger on close.
- Composite widgets follow the expected keyboard model: one tab stop, arrow keys inside, Enter to activate, Escape to close.
- Icon-only controls have an explicit accessible name.
- Meaningful images have alt text. Decorative ones have empty alt. Complex HTML or SVG illustrations get a name or are hidden.
- Interactive visuals (maps, charts) have a list or text alternative.
- Live regions announce dynamic updates (results that recalculate, toasts, counts).
- Never put interactive content inside a hover-only tooltip.
- Custom pan and zoom surfaces set `touch-action` deliberately.
- Reduced motion respected. Nothing flashes more than three times per second.
- Color alone never carries meaning.

## Performance floor

Proposed targets:

- Lighthouse mobile performance 90 or higher, accessibility 100.
- LCP under 2.5 s, CLS under 0.1, INP under 200 ms on a mid-range phone.
- Code-split routes. Marketing visitors should not download an app's charting and data libraries.
- Inline only the first-view critical assets. Lazy-load the rest.
- Large `blur()` filters, stacked drop shadows and full-screen SVG turbulence are expensive. Test on real hardware or avoid.
- `will-change` and `translateZ(0)` stay out unless a measurement shows a problem, and apply only for the length of the animation.
- For values that change every frame, write CSS variables or transforms through refs and keep React state for coarse readouts. Measure before and after.
- Pause or unmount offscreen looping animation and video.
- Measure on a production build, not only the dev server.
