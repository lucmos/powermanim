from manim import *

from powermanim.components.numberslider import NumberSlider
from powermanim.showcase.showcasescene import ShowcaseScene


class NumberSliderShowcase(ShowcaseScene):
    def showcasing():
        return NumberSlider

    def construct(self):
        slider = NumberSlider()
        self.add(slider)
        self.play(slider.tracker.animate.set_value(2), run_time=1)
        self.play(slider.tracker.animate.set_value(-1), run_time=1)
        self.play(slider.animate.shift(LEFT))
        self.play(slider.tracker.animate.set_value(0.5), run_time=1)
        self.play(slider.tracker.animate.set_value(-1.5), run_time=1)
        self.play(slider.tracker.animate.set_value(0), run_time=1)
