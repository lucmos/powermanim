from manim import *

from powermanim import VGroupHighlight
from powermanim.components.vgrouphighlight import AutoHighlightable
from powermanim.showcase.showcasescene import ShowcaseScene


class VGroupHighlightShowcase(ShowcaseScene):
    def showcasing():
        return VGroupHighlight

    def construct(self):
        dots = [
            Dot(radius=0.25, color=color, fill_opacity=0.25).shift(i * RIGHT)
            for i, color in zip(
                range(-2, 3),
                [
                    RED,
                    GREEN,
                    BLUE,
                    YELLOW,
                    PINK,
                ],
            )
        ]

        group = VGroupHighlight(
            *map(
                lambda x: AutoHighlightable(
                    x,
                    active_fill_opacity=1,
                    active_stroke_opacity=1,
                    inactive_fill_opacity=0.3,
                    inactive_stroke_opacity=0.3,
                    scale_active=1.25,
                    scale_about_edge=LEFT,
                ),
                dots,
            ),
            anim_lag_ratio=0.1
        )
        self.add(group)
        self.play(group.highlight(0))
        self.play(group.highlight(1))
        self.play(group.highlight([2, 3]))
        self.play(group.highlight([1, 3]))
        self.play(group.highlight([]))
        self.play(group.highlight([2, 4]))
        self.play(group.highlight([]))
        self.play(group.clear())
        for _ in range(len(group)):
            self.play(group.only_next(), run_time=0.5)
        self.play(group.clear())
        for _ in range(len(group)):
            self.play(group.also_next(), run_time=0.5)

        self.play(group.clear())
