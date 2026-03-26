# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic gamification design project for an MSc course. It contains a proposal for **WalkFit** — a gamified walking/step-tracking mobile app built using the **6D Gamification Framework** (by Werbach & Hunter). There is no implementation code; all work is documentation in Markdown.

## Repository Structure

- `walkfit.md` — The central deliverable. Contains the full 6D framework applied to WalkFit: business objectives, target behaviors, player personas (Alex the Achiever, Sam the Socializer), activity loops, game elements (XP, badges, streaks, groups), ethics/risks, and implementation roadmap.
- `who-benefits.md` — Stakeholder analysis: primary users (weight-management seekers, inactive adults), secondary stakeholders (insurers, employers, corporate wellness programs).
- `why-now.md` — Market justification: fitness app gamification trends, 85% worker disengagement, Bangladesh-specific context (rising obesity, smartphone penetration, Digital Health vision 2030).
- `prompt.md` — UI design prompt written for Google Stitch, describing the core screens and visual style for the app.
- `resources/6d-framework.md` — The blank 6D framework template (the academic rubric/scaffold this project fills in).
- `resources/for-the-win.md` — Reference text: "For the Win" by Werbach & Hunter (Wharton School Press).

## The 6D Framework

The project follows these six design steps:
1. **Define** business objectives — North Star metric: +15% step increase at 12 weeks
2. **Delineate** target behaviors — Keystone: log steps daily; secondary: join groups, cheer teammates
3. **Describe** players — Achievers (XP/levels/streaks) and Socializers (teams/cheers/challenges)
4. **Devise** activity loops — Engagement loop (log → earn XP → badge → share) and progression loop (XP → level → new milestone)
5. **Don't forget** the fun — "World Trekker" travel narrative, virtual continent unlocks, micro-reward animations
6. **Deploy** appropriate tools — Points (1k steps = 10 XP), badges, groups, streaks; step caps and speed audits as anti-gaming safeguards

## Proposed Tech Stack (not yet implemented)

Backend: Better Auth (authentication), MongoDB, GraphQL API with a custom gamification engine for economy rules, streaks, and pilot experiments.
