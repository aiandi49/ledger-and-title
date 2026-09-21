# Ledger & Title

An independent, educational guide to titling vehicles, real estate, and other major purchases in an LLC's name instead of a personal name — what it changes, what it doesn't, and the paperwork in between.

This is a general-breakdown resource, not a ready-to-relaunch template for any single business. It was built by **Lamar Myers**. If you want this structure set up for your own business, see the [Contact page](contact.html) or reach out directly:

- Email: [ai.agent.lamar@gmail.com](mailto:ai.agent.lamar@gmail.com)
- LinkedIn: [linkedin.com/in/lamar-myers-ai](https://linkedin.com/in/lamar-myers-ai)

## What's in here

Seven static pages, no framework, no build step required to run it:

| Page | File |
|---|---|
| Home / hub | `index.html` |
| Vehicles | `vehicles.html` |
| Real estate | `real-estate.html` |
| Other big purchases | `other-assets.html` |
| Formation guide | `formation.html` |
| Risks & FAQ | `risks-faq.html` |
| Contact | `contact.html` |

Shared design system lives in `css/style.css` (Caribbean-palette design tokens, light/dark themes, responsive rules). Shared behavior — theme toggle, font-size stepper, mobile nav — lives in `js/script.js`. Both are loaded by every page, no server-side includes.

## Editing content

The HTML files are already built and ready to deploy as-is. If you want to change copy or add a page later, don't hand-edit the seven `.html` files directly — edit the source instead, so header/nav/footer stay in sync everywhere:

- `build.py` — the shared header, footer, and page shell (used by every page)
- `content_*.py` — one file per page, holding just that page's `<section>` content
- `generate.py` — regenerates all seven `.html` files from the above

To rebuild after an edit:

```bash
python3 generate.py
```

To preview locally:

```bash
python3 -m http.server 4173
# then open http://localhost:4173
```

(or `npm run dev`, which does the same thing.)

## Pushing to GitHub

```bash
cd ledger-and-title
git init
git add .
git commit -m "Initial commit: Ledger & Title guide hub"
git branch -M main
git remote add origin https://github.com/<your-username>/ledger-and-title.git
git push -u origin main
```

## Deploying to Vercel

This is a static site — no build step is required at deploy time, but `vercel.json` and the `build` script in `package.json` are included so Vercel (or you, locally) can regenerate the HTML from source if it's ever edited.

**Option A — Vercel dashboard**
1. Go to [vercel.com/new](https://vercel.com/new) and import the GitHub repo you just pushed.
2. Framework preset: **Other**. Leave the build command as `npm run build`.
3. Deploy — `vercel.json` sets `outputDirectory` to the project root for you, so you do **not** need to touch the Output Directory field. (Vercel's "Other" preset defaults that field to `public/`, which this repo doesn't use — if a deploy ever fails with "No Output Directory named public found," that field was overridden back to `public` somewhere; open **Project Settings → Build and Deployment → Output Directory**, clear/override it to `.`, and redeploy.)

**Option B — Vercel CLI**
```bash
npm install -g vercel
cd ledger-and-title
vercel        # first deploy, follow the prompts
vercel --prod # promote to production
```

Once connected, every push to `main` redeploys automatically.

## Notes

- No external dependencies at runtime beyond two Google Fonts (Fraunces, Public Sans), loaded via `@import` in `css/style.css`.
- Theme and font-size preferences are stored per-visitor in `localStorage`; nothing is sent to a server.
- Content was last checked against current sources (including 2026 FinCEN rule changes referenced on the Real Estate and Formation pages) in September 2026. Rules referenced here change — verify anything load-bearing with a professional before acting on it.
- This site is general educational information, not legal, tax, or financial advice. See the [Risks & FAQ page](risks-faq.html#disclaimer) for the full disclaimer.
