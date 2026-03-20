# WalkFit — Google Stitch UI prompt

Use with [Google Stitch](https://stitch.withgoogle.com/) (Google Labs). Paste the block below as one prompt; refine with follow-ups (e.g. “darker theme,” “more map-heavy,” “simpler social tab”).

**Related project docs:** `walkfit.md`, `why-now.md`, `who-benefits.md`

---

## Prompt (copy from here)

```
Design a mobile app UI (iOS/Android, portrait) called “WalkFit” — a gamified walking and step-tracking app with a “World Trekker” theme: walking feels like traveling virtual routes across continents, not a boring fitness chore.

AUDIENCE & VIBE
- Primary users: adults who want to move more / manage weight but struggle with consistency.
- Two motivation styles: (1) Achievers — points, XP, levels, streaks, badges; (2) Socializers — teams, cheers, optional weekly group challenges (social features must feel supportive, not shaming).
- Emotional tone: encouraging, playful but calm; avoid aggressive “grind” energy. Use rest-friendly language (not guilt).

VISUAL STYLE
- Distinctive, not generic: pick a cohesive palette (e.g. deep teal + warm sand + coral accent, or forest green + cream + gold accents) and one clear display font for numbers/stats and a readable body font.
- Light mode default; optional dark mode mention OK.
- Generous spacing, large tap targets, clear hierarchy. WCAG-minded contrast for text on colored cards.

CORE SCREENS (design 4–6 key screens as a coherent flow)
1) Onboarding: value prop (habit + adventure), permissions note for steps/notifications (trustworthy copy), sign-up / continue.
2) Home / Today: big daily step count, progress toward daily goal, streak indicator, “World Trekker” route map snippet or location pin on a stylized map, primary CTA “Log steps” (MVP manual entry) + secondary “Start walk”.
3) Log steps (modal or screen): numeric input, quick presets (e.g. +1k / +5k), satisfying confirm state (micro-celebration: subtle confetti or map segment “unlocked” preview).
4) Progress / Profile: XP or level bar, badge grid (e.g. First Streak, 100k total steps), history sparkline or weekly summary.
5) Social (optional tab): teams list, weekly challenge card, cheer button, leaderboard that is clearly labeled OPT-IN with privacy-friendly copy; show “private / friends / team only” states.
6) Settings: notifications, rest day / recovery mode toggle, social competition opt-in, data & privacy stub.

COMPONENTS & UX RULES
- Bottom tab bar: Home, Progress, Social (optional badge if disabled), Profile/Settings.
- Cards for goals, challenges, and badges; clear labels for “streak”, “today’s goal”, “route”.
- Empty states: friendly copy for no team / no badges yet.
- Do NOT look like a clinical medical app; it’s wellness / habit, not diagnosis.

DELIVERABLE
- High-fidelity mobile screens, consistent components, and short notes on interaction (e.g. what happens after logging steps). Favor clarity and delight over clutter.
```

---

## Follow-up prompts (optional)

- **Variant A — minimalist:** “Regenerate with fewer colors, more whitespace, single accent, no illustration on Home.”
- **Variant B — map-first:** “Put the stylized world route map as the hero on Home; steps as a secondary ring or chip.”
- **Accessibility:** “Increase contrast, larger type for step count, test colorblind-safe palette.”
- **Ethics copy:** “Surface ‘rest day’ and ‘opt-in competition’ on Settings and Social; add reassuring microcopy.”
