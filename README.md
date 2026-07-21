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

https://github.com/user-attachments/assets/4d32ad4c-2a10-4e5b-b652-1316ba787cdf

---

**Input:**
```
- Topic: Adding a positive and a negative integer
- Objective: Students add integers of opposite sign
- Worked example: (+5) + (−3)
- Misconception: Students ignore the signs and add magnitudes (5 + 3 = 8), or always subtract without tracking direction
```
**Result:**

https://github.com/user-attachments/assets/7142b4a4-edcd-4f21-a3c8-527b8cc59888

---

To run: `cp framework/* . && cp runs/fractions/input.md input.md && ./loop.sh 15`. New concepts go in `input.md` per `framework/template.md`.
