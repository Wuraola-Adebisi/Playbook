# Process: from references to a brief

## Stages

Work in this order for a new build. Skip a stage only when its output already exists.

| Stage | Output | Done when |
|---|---|---|
| 1. Intake | Reference images or links, one line on what is loved, the project name | The owner confirms the set is complete |
| 2. Analysis | Recurring patterns, outliers, extraction notes | The owner agrees the read matches what they love |
| 3. Style identity | Name, definition, keywords, signature moves, anti-patterns | The owner approves the name and the filter |
| 4. Concept | Subject, audience, use cases, scope, reference log for the flows involved | The owner approves scope |
| 5. Content and data | Every page, section and data structure, plus the flow and state inventory | Nothing the build needs is undefined |
| 6. Tokens | CSS variables and framework mapping, plus a contrast table | A style tile renders correctly in a real browser |
| 7. Components | Spec and code per component after a reuse check | Every state exists |
| 8. Pages and flows | Routes, layouts, responsive behavior | Works at 360, 768, 1280 and 1920 px |
| 9. Motion | One signature moment plus responsive feedback | Reduced-motion mode verified |
| 10. QA | Accessibility, performance, cross-browser | The checklist in `build-and-verify.md` passes |
| 11. Case study | Written and visual story | Reads cleanly with no gaps |

For a restyle of an existing build, stages 1 to 3 still apply. For an audit, derive the style identity from what is already built, then judge the build against it.

## Starting a session

Reply first with a five-line restatement of the project, what is Decided, what is Proposed, what is Open, and the next step. Wait for corrections only when something looks wrong; otherwise state the assumption and proceed.

## Inspiration intake

- Screenshots at full size, 10 to 20 per message.
- Which project it is for.
- One line on what is loved: colors, layout, feel, lines, elements.

## Inspiration analysis

What to extract:

- **Color:** ground, hero fill, supporting colors, accents, text color, and the ranges between them.
- **Type:** how many voices (display, label, body, hand-lettered), weights, case, scale contrast.
- **Layout:** grid behavior, whitespace, alignment, composition.
- **Shape and depth:** radius, borders, outlines, shadows, texture.
- **Imagery:** illustration or photo treatment, scale relationships, filler motifs.
- **Line and graphic system:** line weights, dashes, arrows, icons.
- **Motion cues:** what could animate, even from static images.
- **Mood and content structure.**

Method:

1. List what recurs in three or more references. Those define the style.
2. List one-offs. For each, decide: ignore, borrow for one section, or adopt.
3. Write down what the owner loves in their own words and treat it as the priority filter.
4. Note the artists for credit.
5. Produce the style identity first, then the brief.

Hex values read from images are estimates. Sample them and verify contrast before they become tokens.

## Reference ethics

Boards and reference products are scaffolds. Take principles (color relationships, structure, feel) and make original decisions. Never trace, recreate or lightly rework another designer's composition, and never reproduce another product's visual identity because its layout was useful. Credit boards and artists in the case study.

## Pattern research for flows

- Study several real products for a flow before settling on a pattern.
- Compare what repeats and what varies.
- Follow the whole flow where possible: validation, loading, errors, result. A single screenshot hides all four.
- Note what changes on small screens and with touch.
- Mobbin is a good source when its connector is connected. When it is not, say so and use references that can legitimately be viewed.
- Keep a reference log in `docs/reference-log.md`: link, the pattern studied, what was taken, what was changed, why.

Questions to ask of any reference: what is the primary action and how clearly is it shown, how are content and actions prioritized, what happens before, during and after an interaction, how are errors and empty states handled, which details are essential to the task and which belong to that product's brand.

## Style identity template

- **Name:** two or three words, memorable, describes the feel.
- **Definition:** one sentence a stranger could picture.
- **Keywords:** five words that filter every decision.
- **Signature moves:** three to five things that make the style recognizable.
- **The one memorable thing:** where the boldness is spent. Everything else stays quiet.
- **Anti-patterns:** what would break the style.

## Brief template

1. Style name, definition, keywords
2. Reference analysis
3. Color: values, roles, tested contrast pairs, forbidden pairs
4. Typography: families, roles, scale, rules
5. Spacing, layout, shape
6. Imagery and iconography
7. Motion
8. Components and signature moves
9. Voice and tone, with Do and Don't examples
10. Anti-patterns
11. Token starter

Add to every brief: a decision log (Decided, Proposed, Open), a flow and state inventory, a status log, and a section for case study capture.

## Case study capture

Capture while building, because it is hard to rebuild later:

- The reference board and extraction notes
- The brief and decision log, including changes and the reason
- Early and final screenshots of the same screen
- Token setup and a component sheet
- Accessibility and performance results, with numbers
- What went wrong and how it was fixed

Structure: overview and link, role and tools, brief and audience, references and style identity, the system (tokens, type, components), key interactions, process (early versus final decisions), quality results, how the system adapts to other clients, what comes next. State facts and results. Do not oversell. Follow `writing.md`.
