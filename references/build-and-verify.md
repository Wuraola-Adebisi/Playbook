# Build, audit and verify

## Code conventions

Default stack: React with TypeScript, Vite, Tailwind CSS, Git and GitHub, deployed on Vercel. Inspect the project before assuming it.

```
src/
  tokens/        CSS variables and framework mapping
  components/    UI primitives
  features/      project-specific features
  data/          typed config and content
  lib/           utilities (color, time, storage)
  routes/        pages
```

- Content and map data live in typed config, not inside components, wherever reuse is a goal.
- Browser storage is wrapped in try/catch with a working empty state.
- No raw hex or arbitrary values in components.
- ESLint and Prettier on, TypeScript strict.
- Pin dependency versions. `latest` in `package.json` makes builds unrepeatable. Commit the lockfile.
- Add a `.gitignore` (`node_modules`, `dist`, `.env*`).
- The README holds run, build and deploy steps.
- Commits: one concern each, imperative mood, named file adds rather than `git add .`.
- After any deploy, confirm the live URL actually updated before reasoning from it.
- Keep files readable. A one-line-per-function bundle of 40 KB is a maintenance cost; format it before editing.

## Reuse policy

- Check before building: installed libraries, shadcn/ui, Radix, and native elements (`dialog`, `details`, `form`) for dialogs, drawers, accordions, tabs, selects, checkboxes, switches, toasts and form fields.
- Build custom where the behavior or the visual is specific to the product.
- Customize tokens, spacing, type and states so the result does not read as an untouched library template.
- A Tailwind v4 project that resets the default scales needs adaptation. shadcn files use classes such as `text-sm` and `rounded-md` that no longer exist. Edit the copied files to the project's names, map shadcn variables (`--background`, `--primary`) onto semantic tokens, and configure `tailwind-merge` so custom names are not treated as conflicts.
- On Windows, `npx` based CLIs can fail. Install the packages directly and add the component files by hand.
- Record the choice: each component names the primitive it builds on, or the reason it is custom.
- Native `dialog` is a valid choice when no component library is installed. It avoids a dependency and gives focus trapping and Escape for free.

## Component spec (use for shared components)

```
Component: Name
Description: what it is, when to use it
Variants / Props
States: default, hover, focus, active, disabled, loading, error, empty
Responsive: behavior at 360 and 768 px
Motion: what animates, duration, easing, reduced-motion fallback
Accessibility: role, keyboard, announcements, names for icon-only controls
Hit area: visual size versus tappable size
Reuse: primitive used, or why custom
Tokens used
Do and Don't
```

Minimum set per project: button, link, input, textarea, select, checkbox and radio, card, nav, footer, badge, modal or sheet, toast, accordion, tabs, tooltip.

## Audit procedure for an existing build

1. **Sync first.** `git fetch`, then read `git log`, list branches and check which are merged into the main branch (`git branch -r --merged origin/main`). The owner may still be pushing, and screenshots may come from a different branch than the one you cloned. Say which branch you reviewed.
2. **Read.** Structure and file sizes, how many stylesheets or style layers compete, custom properties, counts of raw hex values, font sizes under 12px, radius values and shadow declarations, fonts loaded and whether they are requested twice, remote images and scripts, `package.json` pinning, README, routes, and what is bundled for which visitors.
3. **Look.** Run a production build, serve it, and screenshot at 360, 768 and 1280 px. Seed realistic data in localStorage to see the real states. Also look at the first-run and empty states.
4. **Rank findings.** Mark each as verified in a browser or read in code only. Order them:
   - Breaks the product: wrong numbers, lost data, dead flows.
   - Blocks users: contrast, labels, keyboard, focus, hit areas, zoom on iOS.
   - Weakens trust: generic stock imagery, filler copy, claims the product cannot back, inconsistent branding.
   - Polish: spacing, radius and shadow scales, motion.
5. **Report.** Start with what already holds up, then findings grouped by area, then the suggested order of work, then one question if the answer changes the work.
6. **Fix in batches**, in this order: foundation (tokens, scales, type floor, dead CSS), cuts (remove what does not earn its place), structure (page headings, first run, layouts), states and forms, logic, copy, motion.
7. **After each batch:** typecheck, build, run the flows in a browser, review screenshots, sweep the pages you did not touch for regressions.

## Verification protocol

- Install, typecheck and build before anything else.
- Serve the production build (`vite preview`) and drive it with Playwright. Seed localStorage to reach real states.
- Run `scripts/check_page.py` on each key route. Run `scripts/contrast.py` on every text and surface pair in the palette.
- Exercise each changed flow: open, validate, submit, cancel, Escape, undo, reload.
- Read the console. A clean console is a requirement.
- Treat a passing sandbox run as proof the code is well-formed. Real device checks (a real iPhone and a real Android phone) and a Lighthouse run on the deployed build remain the owner's confirmation.

Known pitfalls in sandboxes:

- Web fonts usually cannot load, so type looks tighter or wider than it will on the owner's machine. Say so.
- Do not `pkill -f` a pattern that also appears in your own command line. It kills your shell.
- Start long-running servers with `setsid nohup ... &` so they survive between commands.
- Full-page screenshots place fixed elements (bottom navigation) mid-page. Check them in a viewport screenshot.
- Changing only the hash does not reload the page. Test hash entry from a fresh load.
- Text selectors such as `button:has-text("Calendar")` can match navigation items. Scope selectors to a container.
- Prettier on a minified file produces a very large diff. Tell the owner before doing it and do it once.

## Pre-ship QA checklist

- [ ] Style tile and tokens match the brief
- [ ] All component states exist (hover, focus, active, disabled, loading, error, empty)
- [ ] 360, 768, 1280 and 1920 px layouts checked, no horizontal scroll
- [ ] Keyboard-only run-through of every flow
- [ ] Screen reader spot check on forms and dynamic regions
- [ ] Contrast table verified with the script
- [ ] Reduced-motion mode checked
- [ ] Every flow has its loading, empty, error, success and disabled states built and reviewed
- [ ] Forms label every field, set input types and autocomplete, prevent duplicate submits and explain errors next to the field
- [ ] Consequential actions offer undo or confirmation
- [ ] Hit areas at least 44 px with no dead gaps
- [ ] Icon-only controls have accessible names
- [ ] Tabular numerals on money, times and counters
- [ ] Tested on a real iPhone and a real Android phone
- [ ] Lighthouse mobile run and noted
- [ ] No console errors, no layout shift on load
- [ ] Real content in every state, no placeholder text
- [ ] Open Graph image and favicon set when the project is public
- [ ] Dependencies pinned, lockfile committed, README has run, build and deploy steps
- [ ] Deployed URL confirmed live

## Handover and git commands

Give the owner exact commands for their machine. On Windows, use PowerShell and say which folder to run them in. Template:

```
cd path\to\Project
git fetch origin
git checkout main
git pull
git checkout -b design/short-name
Expand-Archive -Force path\to\changes.zip -DestinationPath .
npm install
npm run build
git status
git add <each changed path by name>
git commit -m "Imperative summary of the change"
git push -u origin design/short-name
```

Notes to include with it: which files are new, which were replaced, what to delete by hand, what to run to check, and what to do if a merge conflict appears. A patch (`git apply --index file.patch`) is a second option, but line-ending differences on Windows can make a patch fail, so a zip of full files is the safer default.
