# Foundations: tokens, type, color, layout, motion

## Token conventions

- **Two layers.** Primitives hold raw values (`--violet-600`). Semantic tokens hold roles (`--color-accent: var(--violet-600)`). Components use semantic tokens only.
- **Prefixes:** `--color-*`, `--font-*`, `--text-*`, `--space-*`, `--radius-*`, `--shadow-*`, `--ease-*`, `--dur-*`, `--z-*`.
- **Name collisions.** Before adding tokens to an existing stylesheet, list the custom properties already defined and check for overlap. Two files defining the same name as `--a: var(--b)` and `--b: var(--a)` create a cycle, and every value that depends on it silently becomes invalid.
- **Frameworks.** Map semantic tokens into the framework theme through CSS variables. With Tailwind v4, put tokens in an `@theme static` block and reset the default scales (`--color-*: initial`, and the same for text, radius and shadow) so only system values exist. No raw hex and no arbitrary values (`w-[137px]`) in components. A value needed twice becomes a token.
- **Modes.** When a project has scene or theme modes, change only the scene layer. Keep UI chrome constant so text contrast stays guaranteed.
- **Contrast table.** Every palette ships with tested text and background pairs, the ratios, and a list of forbidden pairs. Generate it with `scripts/contrast.py`.
- **Migrating an existing stylesheet.** Replace exact raw values with the matching token by script, then diff the build. Leave near matches alone until someone decides they are the same color.

## Typography

- One or two families, clearly distinct if two. A third only with a strong reason.
- Fluid scale with `clamp()`. Body line length under 70 characters. Serif body gets slightly more line height.
- Sentence case. Headings carry the hierarchy through size and weight, not through decoration.
- Weight around 500 to 700 for headings, depending on the face. Avoid very light weights at small sizes.
- `font-variant-numeric: tabular-nums` for money, timers, counters and table figures so digits do not shift.
- Inputs at 16px or larger. Add `-webkit-text-size-adjust: 100%`.
- Do not change weight on hover or selection if it shifts layout. Style `::selection` to match the palette.
- Load each family once. Subset when the payload matters, use `font-display: swap`, and keep to two or three weights per family.
- A headline can be part of the picture (banners, tags, tilted labels) as long as it stays readable.

## Color and contrast

- Roles first: ground, surface, ink, muted ink, line, accent, accent deep, soft accent, pop, status colors (danger, warning, success), night and on-night text.
- Text on any background: 4.5:1 for body, 3:1 for large text (about 24px, or 19px bold) and for UI boundaries and focus rings.
- Muted text is where most failures hide. Test it on every surface it appears on, including tinted cards.
- Status color never carries meaning alone. Pair it with text or an icon.
- Keep one accent family and at most one supporting hue unless the brief says otherwise.

## Spacing and layout

- 4px base scale: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- A section rhythm token (for example `clamp(56px, 8vw, 112px)`) and one max content width, shared by header, content and footer so edges align.
- Use the framework's default breakpoints. Check 360, 768, 1280 and 1920 px.
- A layout concept goes in the brief as one sentence plus a rough wireframe.
- Cramped usually means three things at once: text below 14px, no spacing scale, and too many boxes. Fix all three.
- Tools lead with the task: the page title, then the primary action, then the data. Marketing pages lead with one promise and one action.

## Shape and depth

- Radius is a small deliberate scale (for example 10, 16, 24, pill), not a different value per component.
- Shadows are either removed on purpose or a small named set. No default grey drop shadow under every card.
- A hard offset shadow on primary buttons is a valid signature move if it is used consistently and the pressed state moves it.
- Borders and dividers exist to separate content, not to decorate.

## Imagery and icons

- One consistent icon style per project.
- Photos must show the product's world. Generic stock lifestyle photography weakens credibility, and hotlinked stock is a performance and privacy dependency. Prefer real product UI, owned imagery or illustration.
- Real text for labels. Never bake text into images.
- Decorative graphics are hidden from assistive technology and set to `pointer-events: none`.
- Open Graph and favicon assets belong to the project, not a third-party host.

## Motion

- **One orchestrated moment per view.** A single sequence beats scattered effects. No fade-and-slide-up on every section, no hover transition on every card.
- **Respond to action.** Motion that shows what changed (open, expand, confirm, insert) is welcome.
- **Ambient motion is rare.** At most one calm ambient element per view.
- **Duration ladder:** micro 120 to 180 ms, standard 240 to 320 ms, emphasis 400 to 600 ms, sequences 600 to 1600 ms.
- **Easing tokens:** standard `cubic-bezier(.2,.8,.2,1)`, pop `cubic-bezier(.34,1.56,.64,1)`.
- **Frequency decides expressiveness.** Routine actions get feedback of 200 ms or less and no flourish. Rare, meaningful moments may be expressive.
- **Proportional movement.** Presses and lifts are a few pixels or a scale near 0.96.
- **Continuity.** Things open from where they came from and close back to it.
- **Interruptible.** A scroll, tap or key press mid-transition is never trapped. Continuous gestures update the interface directly, with no easing delay.
- **Reduced motion.** `prefers-reduced-motion` removes draw-on, parallax, drift and bounces. Content still appears in its final state.
- **Performance.** Animate transform and opacity. Do not animate blur or filters on large areas. Pause offscreen loops.
- Motion never carries the only copy of information.

## Anti-generic checklist

Avoid these unless the brief demands them:

- A warm cream ground with a high-contrast serif and a terracotta accent.
- A near-black ground with a single acid-green or vermilion accent.
- A broadsheet layout: hairline rules, zero radius, dense columns.
- The SaaS card kit: identical rounded cards, one radius everywhere, the same soft shadow, gradient washes, four identical metric tiles with icon chips.
- Template chrome: tracked-out all-caps eyebrows, middle-dot meta strings, arrows appended to every button, spaced dash labels, monospace small labels, a decorative glyph repeated as a divider.
- A scrolling slogan ticker.
- Fade-and-slide-up on every section.
- Accenting one word of a headline.
- Numbered markers on content that is not a sequence.
- A hero that stacks a photo, a fake dashboard, a floating note and a sticker.

Self-critique: write the design plan, then review it against the brief. If any part reads like what you would produce for any similar page, revise it and say what changed. Before finishing, remove one accessory.
