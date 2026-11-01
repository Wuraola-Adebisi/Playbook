# Raising the ambition of a request

Adapted from Felix Rieseberg, "How to be more ambitious: A tutorial for humans with models" (felixrieseberg.com, 13 October 2026). The article describes four kinds of ambition: speed, altitude, depth and range. Speed is skipped here because it needs no technique. The examples below are frontend versions written for this playbook.

Run this pass once after understanding the task (workflow step 2) and again before calling a draft done. Anything it produces is **Proposed** until the owner says yes. The brief and the owner's taste still win, so raising ambition never widens scope silently.

## When to apply and when to skip

Apply it when the request is a task with a bigger outcome behind it (restyle a page, fix a bug in a flow, build a component), when the first draft looks like what any similar page would get, or when the owner says the result feels too safe.

Skip it for small direct edits (a typo, a color swap, a version bump), when the brief fixes the scope, and for taste calls. Altitude works best when there is an outcome to reach. It works worst where the answer is a matter of taste.

## Altitude: ask for the outcome, not the task

Ask what should happen next and what the goal beyond the goal is.

| Task | Outcome | System |
|---|---|---|
| Fix the overflow on the pricing page | The pricing page has no layout break at 360, 768, 1280 and 1920 px | Every key route is checked at those widths before each push |
| Restyle this card | A first-time visitor finds the main action in under five seconds | The design system rejects raw hex and off-scale spacing by check, not by review |
| Add a loading spinner | Every async flow has real loading, empty, error and success states | A switch forces failures so the states stay testable |

A useful tell: if the work would normally need a meeting to decide what to do, the request is probably pitched too low.

Prerequisite from the article: before handing over an outcome, make sure the agent can reach what it needs to check it. For frontend work that means it can build the project, serve the production build, take screenshots, read the console and read the repo history. If one of those is missing, say so and ask for it or work around it.

Ladder to climb one rung at a time:

1. Ask what changed, why, and what to do about it, with all the real material attached.
2. Ask for the few most urgent decisions, each with arguments for and against.
3. Ask for a better process than the one the task assumes, and for evidence from the project's own history that it would have caught problems sooner.

## Depth: do it the way the best people in the field do it

Depth means one level further down, not a bigger task.

- **Use the instruments the professionals use.** Asking a model to act like an expert often changes its vocabulary and not its method. Insist on the method: a real browser instead of a described one, the contrast script instead of eyeballing, Figma variables instead of guessed values, Lighthouse instead of a feeling about speed.
- **Start from the rawest material.** The Figma file, not a screenshot of it. The production build, not the dev server. Real content, not a summary of it.
- **Set a specific, hard target and state it as reachable.** "Make it fast" gets less than "LCP under 1.5 s on a mid-range phone". Goal-setting research summarized in the article found that specific hard goals beat "do your best". Mark any target not in the brief as Proposed.
- **Try to disprove what everyone believes.** Before acting on "the layout feels cramped" or "users miss the button", try to reproduce the belief from raw evidence: measured font sizes, spacing counts, hit areas, a keyboard run-through. Report what holds and what does not.
- **Look for what nobody asked about.** Once inside the material, look for blind spots: a state with no design, a flow with no error path, a dependency loaded twice.
- **Use an outside judge.** Do not grade your own output. Use something that returns a result: typecheck, build, `scripts/contrast.py`, `scripts/check_page.py`, Lighthouse, a Playwright flow, a real device, the owner. Say which one was used.

A reusable request for this, in the playbook's own words: before rewriting the task, state what a top professional would do that was not asked for, name the rawest material they would start from, name their methods and tools, and name what other than the agent or the owner would show the result is right. Then rewrite the task to ask for exactly that.

## Range: bring in the fields the task does not name

Range means looking at the work from more fields than would once have been affordable.

- **Replace the nouns with verbs.** "A landing page" is a noun. "Getting a skeptical stranger to trust a studio and write to it in under a minute" is a verb, and it points at copywriting, proof, performance and trust signals.
- **Assemble the crew.** For an interface, a plausible crew is an art director, a copy editor, a motion designer, an accessibility auditor and a performance engineer. For a red team, a first-time visitor who does not trust the page, a screen reader user, and someone on a slow phone.
- **Use fields for their methods, not their voices.** Do not tell the agent to write like a copy editor. Tell it to do what a copy editor does: cut, read aloud, check every claim against the product. Role play makes a transcript stranger and the result no better.
- **Give the agent a computer and the data.** Range needs tools it can run and material it can read. If it only has chat, it will role play.

## When the ambition stalls

The article ties unambitious requests to self-efficacy: people attempt less when they do not believe it is possible. Three documented levers, in frontend terms:

- **Specific hard goals.** Replace "improve performance" with a number.
- **Seeing it done.** Study three real products that already do the hard thing before settling on a pattern (this is what `process.md` pattern research is for).
- **Permission to fail.** Try the bold version first on a throwaway branch. Keeping it or dropping it is the owner's call.
