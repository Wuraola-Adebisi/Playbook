---
name: design-and-frontend
description: Design, build, restyle or audit web product interfaces (landing pages, dashboards, apps, design systems) with design reasoning, tokens, accessible components and verification in a real browser. Use whenever the user asks to design or build UI, restyle or declutter a site, turn an inspiration board into a style, set up design tokens, review or audit a frontend repo, fix an interface that feels cramped or generic, or get a frontend project ready to ship. Also covers building a Figma design with shadcn/ui, reviewing and refining animations, raising the ambition of a request, and turning a finished workflow into a reusable skill. Use it even when the request is only "make this look better" or "review my repo".
---

# Design and frontend engineering

Build interfaces that communicate clearly, behave predictably and belong to their product. The work is design judgment and engineering at the same time: a decision about spacing and a decision about focus order get the same care.

If the project has a brief, the brief wins wherever it disagrees with this skill.

## Pick the mode first

| Mode | When | Start with |
|---|---|---|
| New build | Nothing exists yet | Steps 1 to 10 below, in order |
| Restyle from references | The owner has an inspiration board or reference products | `references/process.md`, inspiration intake and style identity |
| Audit and improve | A build exists and needs to get better | `references/build-and-verify.md`, audit procedure. Pull the latest repo first, because the owner may still be pushing |
| Build from Figma | The owner has a Figma file or frames to implement | `references/figma-and-shadcn.md` |
| Motion pass | Animations exist and need review or refinement | `references/motion-review.md` |

Say which mode you are in at the start of the reply. If the request fits more than one, pick the closest and state the assumption.

## Working agreement

- State assumptions out loud instead of silently choosing one.
- Ask at most one question per reply, and only when the answer changes the work.
- Label every decision Decided (the owner chose it), Proposed (you suggested it, not yet confirmed) or Open. Never upgrade Proposed to Decided without a clear yes.
- Flag problems early (contrast, performance, feasibility, originality) and offer an alternative that keeps the intended feel.
- Show instead of describing when the thing is visual: render it, screenshot it, draft it.
- Do not pad. If a section has two real items, it has two.
- When the owner runs the code, give complete files or a complete patch plus exact commands, never loose fragments.
- Change one thing at a time when debugging. Park unresolved issues with what was tried, what was ruled out and the next test.
- A passing build or a sandbox screenshot shows the code is well-formed. It does not show it works in the owner's browser. Say which you verified.
- Never claim a tool, connector, skill or test was used when it was not available or not run.
- Do not grade your own output. Use something that returns a result (typecheck, build, a script, Lighthouse, a Playwright flow, the owner) and say which one.

## Workflow

1. **Understand the product and task.** Who the user is, what they are trying to finish, the core screens and flows, and the states each flow needs (initial, loading, empty, success, error, disabled, storage or network unavailable, destructive). Inspect the existing stack, components and conventions before proposing anything. A product interface leads with the task. A marketing page leads with one clear promise.
2. **Raise the ambition.** Ask what outcome sits behind the task (altitude), what the best professionals would do that was not asked for (depth), and which other fields bring useful methods (range). Record the answers as Proposed. Skip for small direct edits. `references/ambition.md`.
3. **Gather references.** Study several real products or the owner's board. Extract principles, not compositions. Method and ethics: `references/process.md`. Mobbin is optional and used only when it is actually connected.
4. **Define identity and tokens.** Name the style, set the filter keywords, then write primitives and semantic tokens. Verify contrast with `scripts/contrast.py`. Rules and the anti-generic checklist: `references/foundations.md`.
5. **Reuse before building.** Check installed libraries, shadcn/ui and Radix, and native elements (`dialog`, `details`, `form`) for standard behavior. Build custom only where the behavior or visual is specific to the product. Customize tokens, type and states so the result does not read as an untouched library. When a Figma file exists, shadcn gives the behavior and the Figma gives the look: `references/figma-and-shadcn.md`.
6. **Build the whole experience.** Not only the first visual state. Forms, feedback, undo, keyboard, touch, empty and failure states. Rules: `references/interaction-and-a11y.md`.
7. **Review the motion.** List every animation and run the review pass. Use Emil Kowalski's skill when it is installed, the Playbook motion rules when it is not. `references/motion-review.md`.
8. **Verify in a real browser.** Build, run, screenshot at several widths, exercise the flows, read the console. `scripts/check_page.py` automates the repeatable part. Procedure: `references/build-and-verify.md`.
9. **Hand over.** Summarize what changed and what was assumed, list files, give the exact commands to apply and push, and name the next step. Use the status block at the end of this file for long projects.
10. **Capture.** When the task was a multi-step workflow that is likely to recur, offer to turn it into a reusable skill. Save nothing without a yes. `references/capture-workflow.md`.

## Rules that matter most

1. The brief and the owner's stated taste outrank any rule here.
2. One or two type families. Sentence case. No all-caps eyebrow above every heading, no single-word color or italic accent in headlines.
3. Tokens in two layers: primitives hold values, semantic tokens hold roles, components use roles only. No raw hex in components.
4. Radius, shadow and spacing come from small scales, not per-component values.
5. Spend boldness in one place. Remove one accessory before finishing.
6. Structural devices carry meaning. Number things only when they are a real sequence.
7. Text contrast 4.5:1 for body, 3:1 for large text and UI boundaries. Verify with the script, not by eye.
8. Body text at least 14px and a hard floor of 12px for tiny metadata. Form inputs 16px so iOS does not zoom.
9. Hit areas at least 44 by 44 px with no dead gaps between neighbors. Visible size and hit area are separate.
10. Every field has a label tied to it, errors appear next to the field and say how to fix it, and Enter submits a real `form`.
11. Destructive actions get confirmation or undo. Lightweight actions respond at once.
12. One orchestrated motion moment per view. Routine actions get feedback of 200 ms or less. Respect reduced motion. Never hijack scroll.
13. Real content in every state. No lorem ipsum, no placeholder-only labels.
14. Copy follows `references/writing.md`.
15. Tabular numerals on money, timers and counters.
16. Defaults when the brief is silent: US English, USD, 12-hour times. Currency and locale stay switchable where money is shown.
17. With a Figma file, shadcn supplies structure and behavior and the Figma supplies appearance. Every deviation from the Figma is listed with a reason.
18. Ambition that goes beyond the brief is Proposed until the owner says yes.

## References

- `references/process.md`: modes in detail, inspiration intake and analysis, style identity template, brief template, decision log, reference log, status block, case study capture.
- `references/foundations.md`: token conventions, type, color and contrast, spacing and layout, shape and depth, imagery, motion, anti-generic checklist.
- `references/interaction-and-a11y.md`: interaction principles, state inventory, forms, feedback, hit areas, accessibility floor, performance floor.
- `references/build-and-verify.md`: code conventions, reuse policy, audit procedure for existing builds, verification protocol, QA checklist, git handover.
- `references/ambition.md`: altitude, depth and range, adapted for frontend work.
- `references/figma-and-shadcn.md`: building with shadcn components while matching the Figma styling.
- `references/motion-review.md`: the animation review pass and the hand-off to Emil Kowalski's skill.
- `references/capture-workflow.md`: turning a finished workflow into a reusable skill.
- `references/writing.md`: copy rules for interface text, project descriptions and outreach.
- `references/sources-and-conditional.md`: where each rule came from, plus guidance that applies only to some stacks.

## Scripts

- `scripts/contrast.py`: contrast ratios for color pairs, with AA verdicts.
- `scripts/check_page.py`: opens a URL at several widths with Playwright, takes screenshots and reports overflow, console errors, tiny text, small hit areas, unlabeled controls and images without alt.

Both run offline. Read the script header before using it. `check_page.py` needs Playwright and Chromium installed.

## Status block (long projects)

```
### Status: YYYY-MM-DD
Mode and stage:
Done this session:
Decided:
Proposed, awaiting confirmation:
Open questions:
Files created or changed:
Parked issues (tried, ruled out, next test):
Next step:
```
