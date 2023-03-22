from manim import *

from powermanim.layouts.arrangedbulletlist import ArrangedBulletList
from powermanim.showcase.showcasescene import ShowcaseScene


class ArrangedBulletListShowcase(ShowcaseScene):
    def showcasing():
        return ArrangedBulletList

    def construct(self):
        rows = [
            Text(row)
            for row in [
                "First row",
                "Second row",
                "Third row",
                "Fourth row",
            ]
        ]
        g_rows = VGroup(*rows).set_opacity(0.25)
        g_rows.target = ArrangedBulletList(
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
