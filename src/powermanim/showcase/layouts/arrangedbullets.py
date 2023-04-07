from manim import *

from powermanim.layouts.arrangedbullets import ArrangedBullets, Bullet
from powermanim.showcase.showcasescene import ShowcaseScene


class ArrangedBulletsShowcase(ShowcaseScene):
    def showcasing():
        return ArrangedBullets

    def construct(self):
        rows = [
            Bullet("First row"),
            Bullet("Second row"),
            Bullet("Elements:"),
            Bullet("First element", level=1, symbol="(1)"),
            Bullet("Second element", level=1, symbol="(2)"),
            Bullet("Third element", level=1, symbol="(3)"),
        ]
        g_rows = VGroup(*rows).set_opacity(0.25).scale(0.9)
        g_rows.target = ArrangedBullets(
            *g_rows.copy(),
            line_spacing=MED_LARGE_BUFF * 1.25,
            left_buff=MED_LARGE_BUFF * 3,
        ).set_opacity(1)

        self.play(
            MoveToTarget(g_rows),
            rate_func=there_and_back_with_pause,
            run_time=3,
        )

        self.wait()
