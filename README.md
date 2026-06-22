# Da Green Coffee Bar

Marketing site for **Da Green Coffee Bar** — a garden coffee bar hidden behind
South Maui Gardens, 35 Auhana Rd, Kihei, HI 96753.

Single-file static site (`index.html`, no framework). Built by Frontline Web Designs.

## Status — PRE-LAUNCH (do not index yet)

The site carries a `noindex, nofollow` tag and is **not yet live**. Before launch,
confirm the items below, then remove the `<meta name="robots">` tag in `index.html`.

**Confirm before going live:**
- **Menu prices** — currently *rough estimates* (Maui/Kihei 2026 ballpark), flagged
  on-page and in code. Replace every `.price` value with the owner's real list.
- **Phone** — `(808) 856-0025` (from TripAdvisor) — confirm it's the bar's direct line.
- **Hours** — listings disagree; using Mon–Sat 6:30a–6p / Sun 7a–6p. Confirm.
- **Owner names / origin story** — add a sentence or two to the "The Garden" section.
- **Photos** — 3 real images wired (storefront, the garden, the neon sign). A clean
  latte and a *Da Green* toast close-up from the owner would lift the menu.

## Images

Optimized web images live in `images/`. Originals are archived in `images/source/`
(gitignored). To regenerate from originals:

```
python build_images.py
```

`contrast.py` audits the palette against WCAG AA.

## Design

Garden-green re-skin: Bricolage Grotesque × Newsreader + Spline Sans Mono;
canopy-green / bone / sage with a clay-coral accent; a hand-drawn vine motif that
draws in on scroll. WCAG 2.1 AA, responsive, reduced-motion aware.
