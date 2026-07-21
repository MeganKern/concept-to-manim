from manim import *


class Lesson(Scene):
    def construct(self):
        W = 1.2
        H = 5.0
        FW = W - 0.08
        LX = -2.5
        RX = 2.5
        TICK_EXT = 0.2
        LABEL_GAP = 0.6

        def make_ticks(cx, bot, n, side):
            g = VGroup()
            for k in range(1, n):
                y = bot + k * H / n
                if side == "left":
                    x0, x1 = cx - W / 2 - TICK_EXT, cx - W / 2
                else:
                    x0, x1 = cx + W / 2, cx + W / 2 + TICK_EXT
                g.add(Line([x0, y, 0], [x1, y, 0],
                           stroke_color=YELLOW, stroke_width=2))
            return g

        def label_at(cx, level, side):
            if side == "left":
                return [cx - W / 2 - LABEL_GAP, level, 0]
            return [cx + W / 2 + LABEL_GAP, level, 0]

        # Beat 1 — Two empty glasses
        left_bar = Rectangle(width=W, height=H,
                             stroke_color=WHITE, stroke_width=2)
        left_bar.move_to([LX, 0, 0])
        right_bar = Rectangle(width=W, height=H,
                              stroke_color=WHITE, stroke_width=2)
        right_bar.move_to([RX, 0, 0])
        self.play(FadeIn(left_bar), FadeIn(right_bar))
        self.wait(1)

        bot_l = left_bar.get_bottom()[1]
        bot_r = right_bar.get_bottom()[1]

        # Beat 2 — Fill left glass 3/4
        h34 = H * 3 / 4
        left_fill = Rectangle(width=FW, height=h34,
                              fill_color=BLUE, fill_opacity=0.8,
                              stroke_width=0)
        left_fill.move_to([LX, bot_l + h34 / 2, 0])
        self.play(GrowFromEdge(left_fill, DOWN))
        self.wait(1)

        # Beat 3 — Fill right glass 1/8
        h18 = H / 8
        right_fill = Rectangle(width=FW, height=h18,
                               fill_color=BLUE, fill_opacity=0.8,
                               stroke_width=0)
        right_fill.move_to([RX, bot_r + h18 / 2, 0])
        self.play(GrowFromEdge(right_fill, DOWN))
        self.wait(1.5)

        # Beat 4 — Ruler on left glass (quarters), then label "3/4"
        left_ticks_4 = make_ticks(LX, bot_l, 4, "left")
        self.play(Create(left_ticks_4))
        self.wait(0.5)

        lv34 = bot_l + h34
        lbl_34 = MathTex(r"\frac{3}{4}", font_size=36)
        lbl_34.move_to(label_at(LX, lv34, "left"))
        self.play(FadeIn(lbl_34))
        self.wait(1)

        # Beat 5 — Ruler on right glass (eighths), then label "1/8"
        right_ticks_8 = make_ticks(RX, bot_r, 8, "right")
        self.play(Create(right_ticks_8))
        self.wait(0.5)

        lv18 = bot_r + h18
        lbl_18 = MathTex(r"\frac{1}{8}", font_size=36)
        lbl_18.move_to(label_at(RX, lv18, "right"))
        self.play(FadeIn(lbl_18))
        self.wait(1.5)

        # Beat 6 — Switch left ruler: quarters → eighths
        self.play(FadeOut(left_ticks_4), FadeOut(lbl_34))
        self.wait(0.5)

        left_ticks_8 = make_ticks(LX, bot_l, 8, "left")
        self.play(FadeIn(left_ticks_8))
        self.wait(0.5)

        lbl_68 = MathTex(r"\frac{6}{8}", font_size=36)
        lbl_68.move_to(label_at(LX, lv34, "left"))
        self.play(FadeIn(lbl_68))
        self.wait(1.5)

        # Beat 7 — Pour right glass into left glass
        h78 = H * 7 / 8
        target_l = Rectangle(width=FW, height=h78,
                             fill_color=BLUE, fill_opacity=0.8,
                             stroke_width=0)
        target_l.move_to([LX, bot_l + h78 / 2, 0])

        target_r = Rectangle(width=FW, height=0.001,
                             fill_color=BLUE, fill_opacity=0.8,
                             stroke_width=0)
        target_r.move_to([RX, bot_r, 0])

        self.play(
            Transform(left_fill, target_l),
            Transform(right_fill, target_r),
            run_time=2,
        )
        self.wait(1.5)

        # Beat 8 — Hold on left container alone (no label yet)
        self.play(
            FadeOut(right_bar), FadeOut(right_fill),
            FadeOut(right_ticks_8), FadeOut(lbl_18),
            FadeOut(lbl_68),
        )
        self.wait(2)

        # Beat 9 — Name the answer
        lv78 = bot_l + h78
        lbl_78 = MathTex(r"\frac{7}{8}", font_size=36)
        lbl_78.move_to(label_at(LX, lv78, "left"))
        self.play(FadeIn(lbl_78))
        self.wait(2)
