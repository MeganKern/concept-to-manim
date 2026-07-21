# concept-to-manim

Ralph loop that takes a math concept and produces a Manim animation. Built with Claude Code (Opus 4.6), Manim CE, no human in the loop.

**Input:**
```
- Topic: Adding fractions with unlike denominators
- Objective: Students find a common denominator and add
- Worked example: 3/4 + 1/8
- Misconception: Students add numerators and denominators separately (3/4 + 1/8 = 4/12)
```
**Result:**

<!-- REPLACE: drag runs/fractions/lesson.mp4 into a GitHub issue, paste the URL here -->

---

**Input:**
```
- Topic: Adding a positive and a negative integer
- Objective: Students add integers of opposite sign
- Worked example: (+5) + (−3)
- Misconception: Students ignore the signs and add magnitudes (5 + 3 = 8), or always subtract without tracking direction
```
**Result:**

<!-- REPLACE: drag runs/integers/lesson.mp4 into a GitHub issue, paste the URL here -->

---

To run: `cp framework/* . && cp runs/fractions/input.md input.md && ./loop.sh 15`. New concepts go in `input.md` per `framework/template.md`.
