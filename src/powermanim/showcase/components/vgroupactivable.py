from manim import *

from powermanim import VGroupActivable
from powermanim.components.vgroupactivable import AutoActivable
from powermanim.showcase.showcasescene import ShowcaseScene


class VGroupActivableShowcase(ShowcaseScene):
    def showcasing():
        return VGroupActivable

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

        group = VGroupActivable(
            *map(
                lambda x: AutoActivable(
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
        self.play(group.activate(0))
        self.play(group.activate(1))
        self.play(group.activate([2, 3]))
        self.play(group.activate([1, 3]))
        self.play(group.activate([]))
        self.play(group.activate([2, 4]))
        self.play(group.activate([]))
        self.play(group.clear())
        for _ in range(len(group)):
            self.play(group.only_next(), run_time=0.5)
        self.play(group.clear())
        for _ in range(len(group)):
            self.play(group.also_next(), run_time=0.5)

        self.play(group.clear())
