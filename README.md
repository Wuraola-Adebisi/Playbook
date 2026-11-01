# Playbook

A design and frontend skill for coding agents. It covers building, restyling and auditing web interfaces, building from Figma with shadcn/ui, reviewing animation, raising the ambition of a request, and capturing finished workflows as new skills.

## Layout

```
SKILL.md          Entry point. Modes, working agreement, workflow, rules.
references/       Detail files that SKILL.md points to.
scripts/          contrast.py, check_page.py, build_master.py
master/SKILL.md   Everything above in one file, generated.
```

## Two ways to install

Install one of these, not both. They have different names so they do not clash, but they trigger on the same requests.

**Single file (simplest).** Use `master/SKILL.md`. The skill name is `design-playbook`. Put it in a folder called `design-playbook` and add that folder to the agent.

- Claude Code: copy the folder to `~/.claude/skills/` for every project, or to `.claude/skills/` inside one project.
- Claude (web or app): zip the `design-playbook` folder and upload it in the skills section of the settings.
- Other agents: use the skills folder that agent documents.

**Modular.** Use the repo root as the skill folder (name `design-and-frontend`). The agent reads reference files only when it needs them, which keeps the context small.

## Editing

Edit the modular files, then rebuild the master:

```
python scripts/build_master.py
```

Do not edit `master/SKILL.md` by hand. The next build overwrites it.

## Scripts

- `scripts/contrast.py` needs only Python 3.
- `scripts/check_page.py` needs Playwright and Chromium: `pip install playwright`, then `python -m playwright install chromium`.

## Related skills

Animation review uses Emil Kowalski's skill when it is installed (`npx skills add emilkowalski/skill`, from emilkowal.ski/skill). It is not bundled here.
