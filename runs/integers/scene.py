from manim import *


class Lesson(Scene):
    def construct(self):
        # Beat 1 — The path
        nl = NumberLine(
            x_range=[-1, 7, 1],
            length=10,
            include_numbers=True,
            include_tip=False,
        )
        self.play(Create(nl))
        self.wait(1)

        # Beat 2 — The walker arrives at zero
        dot = Dot(nl.n2p(0), color=YELLOW, radius=0.15)
        self.play(FadeIn(dot))
        self.wait(1)

        # Beat 3 — Walk forward (0 → 5), then show direction arrow
        self.play(dot.animate.move_to(nl.n2p(5)), run_time=2)
        forward_arrow = Arrow(
            start=nl.n2p(0) + UP * 0.5,
            end=nl.n2p(5) + UP * 0.5,
            buff=0,
            color=GREEN,
            stroke_width=4,
        )
        self.play(Create(forward_arrow))
        self.wait(1)

        # Beat 4 — Label the forward walk
        plus5 = MathTex("+5", color=GREEN).next_to(forward_arrow, UP, buff=0.15)
        self.play(FadeIn(plus5))
        self.wait(1)

        # Beat 5 — Walk backward (5 → 2), then show direction arrow
        self.play(dot.animate.move_to(nl.n2p(2)), run_time=1.5)
        backward_arrow = Arrow(
            start=nl.n2p(5) + UP * 1.2,
            end=nl.n2p(2) + UP * 1.2,
            buff=0,
            color=RED,
            stroke_width=4,
        )
        self.play(Create(backward_arrow))
        self.wait(1)

        # Beat 6 — Label the backward walk
        minus3 = MathTex("-3", color=RED).next_to(backward_arrow, UP, buff=0.15)
        self.play(FadeIn(minus3))
        self.wait(1)

        # Beat 7 — Dim arrows, pulse landing dot, show brace from 0 to 2
        fwd_dim = forward_arrow.copy().set_opacity(0.2)
        p5_dim = plus5.copy().set_opacity(0.2)
        bwd_dim = backward_arrow.copy().set_opacity(0.2)
        m3_dim = minus3.copy().set_opacity(0.2)
        self.play(
            Transform(forward_arrow, fwd_dim),
            Transform(plus5, p5_dim),
            Transform(backward_arrow, bwd_dim),
            Transform(minus3, m3_dim),
        )
        self.play(dot.animate.scale(1.5), run_time=0.3)
        self.play(dot.animate.scale(1 / 1.5), run_time=0.3)

        brace = BraceBetweenPoints(
            nl.n2p(0) + DOWN * 0.5,
            nl.n2p(2) + DOWN * 0.5,
            direction=DOWN,
            color=WHITE,
        )
        self.play(Create(brace))
        self.wait(1)

        # Beat 8 — Name the answer
        answer = MathTex("= 2", color=WHITE).next_to(brace, DOWN, buff=0.2)
        self.play(FadeIn(answer))
        self.wait(2)
