from manim import *
from scipy.special import softmax

from powermanim.components.chartbars import ChartBars
from powermanim.showcase.showcasescene import ShowcaseScene


class ChartBarsShowcase(ShowcaseScene):
    def showcasing():
        return ChartBars

    def construct(self):
        axes = Axes(x_range=[0, 6], y_range=[0, 1.5], x_length=7, y_length=4)
        size = 5
        changes = 3

        dist1 = softmax(np.random.randn(size))

        bars = ChartBars(axes, dist1, xs=list(range(size)), fill_color=RED, stroke_width=0.1)
        self.add(axes, bars)
        for i in range(changes):
            dist2 = softmax(np.random.randn(size))
            self.play(bars.animate.set_values(dist2), run_time=2)
        self.play(bars.animate.set_values(dist1), run_time=2)
