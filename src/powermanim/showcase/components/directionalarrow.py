from manim import *

from powermanim import DirectionalArrow
from powermanim.showcase.showcasescene import ShowcaseScene


class DirectionalArrowShowcase(ShowcaseScene):
    def showcasing():
        return DirectionalArrow

    def construct(self):
        old_start = Circle(color=GREEN).move_to(LEFT * 2)
        old_end = Circle().move_to(RIGHT * 2).shift(UP * 0.25)
        old_arrow = Arrow(old_start, old_end)
        VGroup(old_start, old_end, old_arrow).shift(UP * 2)

        new_start = Circle(color=GREEN).move_to(LEFT * 2)
        new_end = Circle().move_to(RIGHT * 2).shift(UP * 0.25)
        new_arrow = DirectionalArrow(new_start, new_end)
        VGroup(new_start, new_end, new_arrow).shift(DOWN * 2)

        self.add(old_start, old_end, new_start, new_end)

        self.play(
            AnimationGroup(
                GrowArrow(old_arrow),
                GrowArrow(new_arrow),
                lag_ratio=0.5,
            ),
            rate_func=there_and_back_with_pause,
            run_time=5,
        )
