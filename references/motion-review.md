# Motion review: use Emil Kowalski's skill for the animation pass

Owner instruction: use Emil Kowalski's design engineering skill to review and refine the animations.

Emil Kowalski publishes agent skills on animation and interface polish. His site (emilkowal.ski/skill) gives the install command `npx skills add emilkowalski/skill`. Public listings of the repository name three skills: `emil-design-eng` (the main skill, mostly animation plus some design advice), `review-animations` (a strict review of animation code) and `improve-animations` (an audit of every animation in a codebase with prioritized plans). Check the installed skill list for the exact names in the current session, because they may change. If the install fails, check the repository name on his site, since listings spell it two ways.

The Playbook does not copy his skill. It points to it.

## When to run the pass

After the motion is built and before verification (workflow step 7). Also when the owner asks for animation to be reviewed or refined.

## Procedure

1. **List every animation.** Name each one: what triggers it, what moves, duration, easing, and whether it runs on a frequent or a rare action.
2. **Check whether the skill is available.** Look at the installed skills.
   - If it is available, run it as the reviewer over that list and the code. Use the output format it defines. If it defines none, ask for findings as a table of before, after and why.
   - If it is not available, say so in one line, offer the install command, and review against the motion rules in `foundations.md` instead. Never say his skill was used when it was not.
3. **Refine.** Apply the findings in small commits. Change one animation at a time so a regression can be traced.
4. **Check the floor.** Reduced motion is respected, only transform and opacity animate on large areas, nothing traps input mid-transition, and no animation carries the only copy of information.
5. **Hand over feel to the owner.** A sandbox run shows the code runs and respects reduced motion. Whether it feels right is confirmed on a real device by the owner.

## Which rule wins

Proposed order, to be confirmed by the owner:

1. The brief and the owner's stated taste.
2. The specific values and verdicts from the reviewer skill when it ran.
3. The Playbook's duration ladder and defaults in `foundations.md`.

Where the reviewer's numbers are tighter than the ladder, use the tighter numbers for routine interface transitions and keep the ladder's longer steps for the one orchestrated moment per view.

## What to ask the reviewer for

- A verdict per animation, with a keep, change or remove call.
- For each change: the current value, the proposed value and the reason.
- Anything that animates too often to deserve animation at all.
