# Figma to shadcn: build with shadcn, look like the Figma

Owner instruction: use shadcn components, but match the Figma styling as closely as possible.

The split: **shadcn supplies structure and behavior** (Radix primitives, keyboard model, focus handling, ARIA). **Figma supplies appearance** (color, type, spacing, radius, shadow, state styling). Where the two meet, edit the component files so they look like the Figma. Do not leave them looking like shadcn defaults, and do not rebuild the behavior by hand.

## Steps

1. **Read the Figma first.** List the frames, components, variants and the variables or styles for color, type, radius, shadow and spacing. If a Figma connector is available in the session, use it and say so. If it is not, work from exports or screenshots, label every measured value an estimate, and sample colors before they become tokens. Never claim Figma data was read when it was not.
2. **Turn Figma values into tokens.** Figma variable names become primitives. Roles (ground, surface, ink, accent, line) become semantic tokens. Components use semantic tokens only. Rules are in `foundations.md`.
3. **Match each Figma component to a primitive.** Dialog, sheet, select, tabs, accordion, tooltip, toast, checkbox, switch, radio and form fields usually map to a shadcn component. If nothing fits, build it custom and record why (`build-and-verify.md`, reuse policy).
4. **Restyle the copied shadcn files.** They live in the project, so edit them. Change variants (with `cva` where the project uses it), sizes, radius and states to the Figma values using the project's token classes. Map shadcn variables (`--background`, `--primary`, `--radius` and the rest) onto semantic tokens. Avoid `!important`, wrapper CSS that fights the component, and per-use class overrides that repeat. On a Tailwind v4 project that reset the default scales, replace classes such as `text-sm` and `rounded-md` in the copied files first.
5. **Keep the behavior.** Leave the keyboard model, focus management, `aria-*` and portal behavior alone. A visible focus ring stays, restyled to the palette.
6. **Fill the states Figma does not show.** Most Figma files show default and sometimes hover. Focus, active, disabled, loading, error and empty usually have no frame. Design them from the token system and list them as Proposed until the owner confirms.
7. **Compare against the frame.** Render the component at the frame's width and set it beside the Figma frame. Check computed styles (font size, line height, padding, radius, color, shadow) against the Figma values. Report each difference with a reason or fix it.
8. **Record it.** In the component spec, name the primitive used, the Figma frame or node link, and the deviations.

## Where Figma and the accessibility floor disagree

Figma files often contain muted text under 4.5:1, targets under 44 px, or inputs under 16 px. Do not copy these silently and do not override them silently. Flag the issue, give the measured value, and propose the smallest change that keeps the intended look (a slightly darker muted ink, extra padding that enlarges the hit area without changing the visible size). List it under Proposed. The owner decides.

## Done when

- The component is built on a primitive, or the reason it is custom is written down.
- Computed styles match the Figma values, or each difference is listed.
- Every state exists and has been looked at, not only default and hover.
- The component works with the keyboard alone.
- No raw hex, no arbitrary values, no leftover shadcn default look.

## Pitfalls

- On Windows, `npx` based shadcn commands can fail. Install the packages directly and add the component files by hand.
- shadcn components merge classes with `tailwind-merge`. Custom token names need to be registered there or they will be treated as conflicts and dropped.
- A visual match in a screenshot does not prove the hover, focus and pressed states match. Drive them in a real browser.
