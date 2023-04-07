from manim import *

from powermanim.components.vgrouphighlight import VGroupHighlight
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

        group = VGroupHighlight(*dots, anim_run_time=1, anim_lag_ratio=0.1)
        self.add(group)
        self.play(group.highlight(0))
        self.play(group.highlight(1))
        self.play(group.highlight([2, 3]))
        self.play(group.highlight([1, 3]))
        self.play(group.highlight([]))
        self.play(group.highlight([2, 4]))
        self.play(group.highlight([]))
        self.wait(0.5)
