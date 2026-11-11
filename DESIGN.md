# DESIGN.md: The Unbound Nomad (unboundnomad.com)

How this site should look, read, and behave. Any person or AI session changing the site reads this first. If a change conflicts with this file, follow this file or ask Phil.

This file lives in the repo root on the `content` branch. It is not published (Pelican only builds `content/`).

## Who it's for and what it's for

- **The site:** the home base for The Unbound Nomad: Phil's motorcycle stories, ride guides, rider resources and the MotoPin app, plus guided rides and concierge trip planning.
- **Readers:** motorcycle riders, mostly touring and cruiser riders in the US Midwest and Southeast, many reading on a phone.
- **What a visit should lead to:** read a story or guide, then follow on social, get MotoPin or a free guide, or book a ride.

## Voice

- First person, from Phil. Plain, direct, warm. Short sentences. No hype words, no corporate tone.
- **Phil is a "biker," never a "rider."** Other people are riders.
- Stick to what's true. Don't invent details about rides, people, places or feelings; leave a gap for Phil to fill.
- Never make up riding rules or safety rules on Phil's behalf (no "only tap when parked"-style advice). Phil rides and decides.
- **The bike:** a 2026 Indian Roadmaster Dark Horse. Its name is **Tȟašína Máni** ("Tasha"), Phil's choice. Keep the accents exact. Never say fans or a vote picked it. Don't put the name on the site until the name reveal reel is live.
- Earlier bikes (Lozen, Gouyen) are only ever mentioned in the past tense.
- Tagline: **RIDE • EXPLORE • REMEMBER**. Service line: "You show up. I handle the rest."
- Social: Facebook, Instagram, TikTok, YouTube only. Instagram and TikTok are **@unbound_nomad**. No Reddit or forums.
- Trip stories (for example the Tail of the Dragon) don't advertise guided rides or booking.

## Colors

Defined in `content/extra/custom.css`. Use these; don't introduce new brand colors.

| Role | Value | Where |
|---|---|---|
| Sidebar / darkest purple | `#1a0028` | sidebar background, hero gradient start, theme-color |
| Hero gradient end | `#2d0050` | `.un-hero`, CTA bands in posts |
| Button purple | `#4a1878` | `.un-btn` background |
| Brand purple | `#603090` | links, accent (`--unbound-primary`) |
| Brand green | `#90a800` | button text, hover accent, logo (`--unbound-secondary`) |
| White | `#ffffff` | text on dark purple, button hover text |
| Footer grey | `#666666` | footer text (readable on white, about 5.7:1) |

Rules:
- Text on dark purple is white (or white at 85–90% opacity for body copy).
- Green is an accent for button text, highlights and the primary button inside the dark hero. It's never used for body text on white.

## Type

- **Font:** Source Sans Pro (loaded by the Flex theme). No second typeface.
- Headings are light (weight 400) with slight letter spacing; uppercase only on buttons.
- Body line height 1.7–1.8 for long reads.
- Post metadata (date, category, tags) is small and softened.

## Layout

- Flex theme: dark purple sidebar on the left (logo, page menu, social icons), content on the right. On phones the sidebar stacks on top.
- Sidebar menu = pages with `Status: published`. Keep it short; pages that shouldn't be in it use `Status: hidden`.
- Content column only. No full-bleed sections outside the theme's main column.
- Phones first: check every new page at about 390 px wide. Nothing scrolls sideways.

## Components

Reuse these classes instead of writing new inline styles.

- **`.un-btn`:** the one button style. Purple background, green uppercase text, white text on hover. Use for one main action per section.
- **`.un-btn-ghost`:** outlined secondary button next to a `.un-btn`.
- **`.un-hero`:** homepage call-to-action band (dark purple gradient, white headline, a green primary button and a ghost button).
- **Cinematic hero (posts):** the full-width photo with title overlay used at the top of ride posts. Existing posts use inline styles; copy an existing post's block when making a new one.
- **`.un-shots`:** a row of 2–3 images side by side (screenshots, photo sets).
- **`.un-video`:** responsive 16:9 wrapper for YouTube embeds. Always `youtube-nocookie.com`, `loading="lazy"` and a `title`.
- **`.un-embed-loading`:** spinner placeholder for third-party forms (Jotform, MailerLite). Give it `data-watch` and, when there's a direct link, `data-fallback`.

## Images

- **Phil's own photos and footage stills only.** No stock photos and no AI-generated scenery. App screenshots come from MotoPin's store listing.
- Raw footage never goes on the site; stills come from finished, posted edits.
- Every image has real `alt` text that describes what's in it, never a file name.
- Sizes: up to about 1600 px wide for full-width photos, 480–640 px for side-by-side shots, JPG quality about 82–85. Strip location data.
- Every page has a share image: set `Og_image:`, or the first image in the post is used, falling back to `images/og-default.jpg`.

## Page basics (every new page or post)

- `Description:` metadata, about 150 characters, written for search results.
- One `<h1>` (the title); sections use `##`.
- Legal pages stay `Status: hidden` and are linked from the footer and related pages, not the menu.
- Dates in the future don't publish (`WITH_FUTURE_DATES = False`). Drafts aren't built at all.

## Don'ts

- No stock or AI imagery, gradients other than the brand purple ones, new fonts, emoji-heavy headings, or pop-ups.
- No cards nested in cards, no icon tiles above every heading, no gray text on colored backgrounds.
- Don't edit the Flex theme repo; put template changes in `theme_overrides/templates/`.
