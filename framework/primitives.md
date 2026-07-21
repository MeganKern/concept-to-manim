# PRIMITIVES — the only visual vocabulary

Every lesson is built from these 8 primitives (compositions allowed). Each maps a
physical intuition a child already has to the math it unlocks. The snippets are
illustrative Manim Community; adapt sizes/positions to the storyboard.

The most important note on each is the **affordance**: what it makes the viewer
want to do. Choose primitives whose affordance matches the *correct* operation and
avoids the wrong one named in `diagnosis.md`.

---

## 1. Container + Fill
Physical intuition: a glass, a battery, a loading bar — *how much you have*.
Unlocks: fractions, percent, probability, part–whole, "amount."
```python
bar  = Rectangle(width=W, height=H, stroke_color=WHITE, stroke_width=2)
fill = Rectangle(width=W*frac, height=H, fill_color=BLUE, fill_opacity=0.8, stroke_width=0)
fill.align_to(bar, LEFT)                 # anchor fill to the container's left edge
self.play(Create(bar))
self.play(GrowFromEdge(fill, LEFT))      # the level "rises"
```
Affordance: a *continuous amount*. ⚠ If you draw internal division lines, the bar
becomes countable cells — that affords COUNTING. Do not divide the fill when the
misconception is a counting / whole-number error.

## 2. Position on a line
Physical intuition: standing somewhere, walking to somewhere.
Unlocks: integers, add/subtract, number sense, inequalities, irrationals.
```python
nl  = NumberLine(x_range=[-6, 6, 1], include_numbers=True)
dot = Dot(nl.n2p(0), color=YELLOW)
self.play(Create(nl), FadeIn(dot))
self.play(dot.animate.move_to(nl.n2p(3)))                 # travel here → there
arrow = Arrow(nl.n2p(0), nl.n2p(3), buff=0)               # direction of travel
brace = BraceBetweenPoints(nl.n2p(0), nl.n2p(3))          # the gap covered = answer
```
Affordance: travel and direction. Good when the operation is "move / how far / which way."

## 3. Physical transfer
Physical intuition: moving stuff from one place to another; nothing is created or destroyed.
Unlocks: addition, combining like terms, conservation, solving equations (move across `=`).
```python
self.play(piece.animate.move_to(target_slot.get_center()))   # A → B, total conserved
```
Affordance: combining with conservation. Use for "put together / take from / carry over."

## 4. Scaling
Physical intuition: the SAME thing, just more or less of it.
Unlocks: multiplication, dilation, proportional relationships, similarity.
```python
self.play(shape.animate.scale(2))                            # grow in place
self.play(shape.animate.scale(2, about_point=center))       # dilation from a center
```
Affordance: same shape/identity at a new size. Good when quantity changes but kind doesn't.

## 5. Measurement overlay  (ALWAYS after the amount already exists)
Physical intuition: laying a ruler on something to say how much it is.
Unlocks: naming a quantity, unit conversion, amount → number.
```python
xs = [bar.get_left()[0] + k*(W/n) for k in range(1, n)]     # n equal sections
ticks = VGroup(*[
    Line([x, bar.get_bottom()[1]-0.1, 0], [x, bar.get_top()[1]+0.1, 0],
         stroke_color=YELLOW, stroke_width=1.5) for x in xs])
self.play(Create(ticks))                                    # now count where the fill lands
```
Affordance: reading a number off a physical amount. The overlay is the LAST step,
never the first — the amount must be understood before it is measured.

## 6. Side-by-side comparison
Physical intuition: holding two things next to each other.
Unlocks: equivalence, inequality, ratio, unit rate.
```python
VGroup(a, b).arrange(DOWN, buff=1.0)                         # same frame of reference
link = DashedLine(a.get_corner(DR), b.get_corner(UR))       # tie corresponding features
```
Affordance: "these are the same / that one is bigger." Keep the shared reference
identical (same width, same baseline); differ in exactly one dimension.

## 7. Transformation
Physical intuition: watching a thing slide, flip, or spin.
Unlocks: congruence, similarity, rigid motions, symmetry.
```python
self.play(ReplacementTransform(shapeA.copy(), shapeB))      # A becomes B
self.play(shape.animate.rotate(PI/2))                       # or .shift / flip
# DashedLine between matching vertices shows the correspondence
```
Affordance: "it's still the same thing, just moved." Good for "did it change or not?"

## 8. Tracing  (no updaters — pre-compute the path)
Physical intuition: a path being drawn as something moves.
Unlocks: functions, slope, graphing, rate of change.
```python
axes  = Axes(x_range=[0, 6, 1], y_range=[0, 6, 1])
graph = axes.plot(lambda x: m*x + b)                        # precomputed curve
dot   = Dot(color=YELLOW).move_to(graph.get_start())
self.play(Create(axes), Create(graph))
self.play(MoveAlongPath(dot, graph))                        # a point rides the relationship
rise  = BraceBetweenPoints(p1, p2); run = BraceBetweenPoints(p2, p3)   # slope = steepness
```
Affordance: steepness = fast/slow, rise over run. Draw the path with `Create`; ride
it with `MoveAlongPath`. Do NOT use a traced-path updater.

---

## Common compositions (molecules built from the atoms above)
- **Partition into equal parts** = a Rectangle `ReplacementTransform`-ed into a
  VGroup of equal sub-rectangles. ⚠ This affords COUNTING — avoid it when the
  misconception is a counting / whole-number error; prefer Container+Fill instead.
- **Pour / transfer volume** = two Container+Fills; one fill shrinks (`.animate.stretch`
  on y) while the other grows — total conserved.
- **Balance / equation** = a `Line` beam + a `Triangle` fulcrum + weighted VGroups
  at equal distances; `.animate.rotate` tips it; add/remove equally to keep level.
- **Walk a distance** = Position-on-a-line + `Brace` for the gap + `Arrow` for direction.

---

## SANDBOX CONSTRAINTS (hard)
- Manim Community. Exactly one `Scene` subclass named `Lesson`; all logic in `construct`.
- **No updaters.** No `add_updater`, no `always_redraw`, no ValueTracker-driven
  redraw. Pre-compute all geometry; animate only with the verbs below.
- **Known-good verbs only:** `Create`, `Write`, `FadeIn`, `FadeOut`, `GrowFromEdge`,
  `GrowFromCenter`, `Transform`, `ReplacementTransform`, `MoveAlongPath`, and
  `.animate` for `move_to` / `shift` / `scale` / `rotate` / `stretch` / `align_to`.
  Always put `self.wait(...)` between beats.
- **No external assets** — no images, SVGs, custom fonts, or audio. Text only via
  `Text` / `MathTex`, and only after its physical referent (Iron Rule 3).
- **Deterministic** — no randomness. Colors via Manim constants (BLUE, GREEN, YELLOW, WHITE…).
- Single fixed 2D frame; keep every object within view; do not rely on 3D or camera moves.
