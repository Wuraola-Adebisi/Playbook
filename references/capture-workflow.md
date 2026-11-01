# Capture the workflow as a reusable skill

Owner instruction: turn the workflow you just completed into a reusable skill for future tasks.

## When

- The owner asks for it.
- A multi-step task has just finished and the same task is likely to come back (auditing a repo, restyling from a board, a Figma to shadcn build, a pitch mockup, a case study).
- The same workflow shows up a second time. Propose capturing it then. Do not save anything without the owner's yes.

## Procedure

1. **Replay what happened, in order.** Steps, commands, files touched, decisions, dead ends and what fixed them. Work from the conversation and the repo history, not from memory of how it felt.
2. **Separate the procedure from the specifics.** Keep what would be true next time. Strip project names, client names, URLs, keys, personal data and one-off values. Nothing private goes into a skill file, because skill files get pushed to repos.
3. **Write the skill body.** Inputs needed, steps in order, checks that prove each step worked, outputs, and the failures actually met with the fix for each. Leave out the story of the session.
4. **Write the description for triggering.** It says what the skill does and when to use it, including the loose phrasings an owner would really type ("make this look better", "review my repo").
5. **Decide where it lives.** A step in the design and frontend pipeline becomes a section or reference file in this playbook. A workflow with different triggers (cold outreach, case study writing) becomes its own skill.
6. **Keep it small.** Body under about 500 lines. Long detail goes in `references/`. A command run the same way every time becomes a script.
7. **Test it once.** Run it on a fresh task or replay the old one with only the skill as guidance. Fix what the run exposes. If a skill-creation skill is available in the session, use it for this step.
8. **Owner confirms** before it is saved or pushed. Commit with a message that describes the change. No co-author trailers.

## Skeleton

```
---
name: short-kebab-name
description: What it does. Use when <situations and phrasings>.
---

# Title

## Inputs
## Steps
## Checks
## Outputs
## Failures seen and fixes
```

## Quality bar

- Someone who was not in the session could follow it.
- Every step has a check or a visible result.
- The description would trigger on the owner's real phrasings and would not trigger on neighboring tasks.
- Follows `writing.md`.
