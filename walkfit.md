## WalkFit — project overview

**WalkFit** is a **mobile-first, gamified walking app** for people who want to move more (especially for weight and general health) but struggle to stay consistent. Users **log daily steps** (manual at MVP, automated tracking later), get **immediate feedback** through points, streaks, and level-style progress, and can **join groups** for social challenges and light competition—optional by design so pressure stays healthy.

The experience is framed as **“World Trekker”**: walking unlocks **virtual routes and badges** so the habit feels like exploration, not homework. The design intentionally serves two motivations—**achievers** (XP, goals, milestones) and **socializers** (teams, cheers, leaderboards)—with **anti-cheat caps** and **anti-grind** limits so the game doesn’t push unsafe or fake behavior.

A short **implementation path** is sketched at the end: MVP auth and data (**Better Auth**, **MongoDB**), then a **GraphQL** API and **gamification engine** (economy rules, streaks, pilot experiment).

The sections below follow the **6D gamification framework** (objectives → behaviors → players → loops → fun → tools) so the proposal maps cleanly to the assignment template.

---

### **PART 1 — Define Business Objectives**

_Goal: Clearly articulate the problem and how you’ll measure success._

- **1.1 Business Objective Statement:**
  - **Problem:** Many people move very little day to day—they sit for work, commute by car, and relax on the couch. Over time, that lack of movement makes it easier to gain weight and raises the risk of health problems tied to inactivity. Walking is simple, cheap, and good for you, but it’s also easy to put off: it can feel boring, and most of us don’t wake up excited to “go for a walk” the way we might for other habits. So even when someone _wants_ to be healthier, they often struggle to stick with walking regularly.
  - **Why Now:** Health care and lost productivity from preventable, lifestyle-related illness keep getting more expensive—so there’s real pressure to help people move more _before_ problems get serious. That lines up with **Define Business Objectives:** inactivity isn’t just a personal habit issue; it’s missed outcomes and rising cost. Meanwhile, people already use phones for steps, reminders, and daily apps; you don’t need special gear or a gym to try something new—and mobile games and gamified habit apps have shown at scale that points, goals, and social hooks can keep people coming back. Most fitness apps already borrow those same ideas, and gaming is a mass-market industry, so feedback and rewards feel familiar, not weird. **WalkFit** sits in that sweet spot: urgent need, a device everyone carries, and mechanics users already understand. _(Stats, examples, and Bangladesh angle: [why-now.md](why-now.md))_
  - **Who Benefits:** **End users** first—people who want to lose weight or move more but need structure, feedback, and optional social accountability (achievers + socializers). **Organizations** second—insurers and employers who want scalable, phone-based wellness participation (challenges, opt-in leaderboards, aggregated engagement)—without claiming clinical treatment. _(Segments, stakeholder logic, and caveats: [who-benefits.md](who-benefits.md))_
  - **Business Value Hypothesis:** Gamification will increase daily engagement and turn a "boring" task into a rewarding habit.

- **1.2 Success Metrics:**
  - **North Star Metric:** Average daily steps per active user (how consistently people move).
  - **Target:** +15% steps on average over 12 weeks.
  - **Leading indicators (early signals):**
    - **D7 retention:** how many users come back after 7 days.
    - **Logging rate:** % of days where a user records steps (a “doing the habit” signal).
    - **Streak health:** streak completion rate _and_ average streak length (we want consistency, not burnout).
  - **Guardrails (what not to hurt):**
    - **Safety flags don’t rise:** the app should not increase “over-exertion” reports or negative feedback (measured via quick check-ins and support/feedback tags).
    - **Anti-cheat works:** unrealistic step patterns should be detected and treated fairly (so results reflect real behavior).
- **1.3 Ethics & Risk:**
  - **Potential Harm 1 (electronic whip):** People may feel pressured to hit the goal every day, which can lead to over-exertion or anxiety.
  - **Mitigation:** Add a **rest day / recovery mode**, allow streaks to pause (so missing a day doesn’t feel like failure), and keep goal increases gradual.
  - **Potential Harm 2 (unsafe/cheating behavior):** Users might try to “farm” points with fake steps or extreme targets that aren’t safe.
  - **Mitigation:** Put caps on daily scoring, detect impossible step spikes, and validate progress with “reasonable range” rules (then explain simply in the UI when something is flagged).
  - **Potential Harm 3 (social pressure):** Leaderboards can shame some users or discourage beginners.
  - **Mitigation:** Social features are **opt-in**, let users choose **team-only or private** visibility, and avoid public comparisons by default.
  - **Potential Harm 4 (privacy):** Step and activity data can feel personal.
  - **Mitigation:** Use **data minimization** (only what you need), get clear consent for notifications, and provide an easy way to adjust goals and opt out of social features.

---

### **PART 2 — Delineate Target Behaviors**

_Goal: Specify the smallest actions you want from players._

- **2.1 Behavior Map:**
  - **Keystone Behavior (Verb):** **Log** steps daily (Manual MVP, automated future).
  - **Supporting Behaviors:** **Join** a group, **cheer** a teammate, **view** leaderboard.
  - **Trigger:** Daily push notification ("quest prompt") $\to$ **Action:** Walking $\to$ **Feedback:** Points and streak level bar.
- **2.2 Anti-behaviors & Safeguards:**
  - **Unwanted Behavior:** "Gaming the system" (shaking the phone for fake steps) [2.3, 384].
  - **Safeguard:** Implement caps on daily steps and audits for impossible speed intervals.

---

### **PART 3 — Describe Your Players**

_Goal: Design for diverse motivations._

- **3.1 Primary Personas:**
  - **"Alex" (Achiever):** Motivated by "Hard Fun"; focuses on **Points** and **Levels**.
  - **"Sam" (Socializer):** Motivated by "People Fun"; stays active to help their **Group** win the weekly challenge.
- **3.2 Target Aesthetics (MDA Framework):**
  - **Achievement:** Emotional response from hitting a milestone.
  - **Fellowship:** Connection felt through group leaderboards and cooperative goals.

---

### PART 4 — Devise Activity Loops

_Goal: Tie actions to immediate feedback and visible progress._

- **4.1 Engagement Loop:**
  - **Motivation:** Desire to keep a 5-day streak.
  - **Action:** Completing a 10,000-step walk.
  - **Immediate Feedback:** Visual confetti and "Level Bar" movement.
- **4.2 Progression System:**
  - **Novice $\to$ Pro:** As users progress, daily step goals increase, and they unlock new "World Map" routes or badges.
  - **Anti-Grind:** Limit point gains after extreme thresholds to prevent burnout.

---

### **PART 5 — Don’t Forget the Fun!**

_Goal: Engineer delight and theme._

- **5.1 Theme & Narrative:** Use a **"World Trekker"** metaphor. Users aren't just walking; they are "traveling" across virtual continents.
- **5.2 Game Feel (Feedback & Polish):**
  - **Micro-rewards:** "Satisfying sound + subtle animation" when steps are logged.
  - **Time to Feedback:** Instant updates (<300ms) to the progress pulse.

---

### **PART 6 — Deploy the Appropriate Tools**

_Goal: Select specific mechanics to serve behaviors._

- **6.1 Element-Behavior-Metric Matrix:**
  - **Points:** 1,000 steps = 10 XP; tracks daily performance.
  - **Groups/Teams:** Drives the "Socializer" persona through cooperative weekly rankings.
  - **Badges:** Visual markers for "1st Streak" or "100k Total Steps".
- **6.2 Pilot Experiment Plan:**
  - **Hypothesis:** Daily streaks increase 7-day retention by 10%.
  - **Variant:** Control group (no streak) vs. Treatment group (visible streak bar).
- **6.3 Implementation Roadmap:**
  - **Week 1-2:** MVP Development (Auth via Better Auth + MongoDB Schema).
  - **Week 3-4:** Gamification Engine & GraphQL Polish.
