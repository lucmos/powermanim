import numpy as np
from manim import *
from scipy.special import softmax

from powermanim.components.chartbars import ChartBars


def test_barcharts():
    with tempconfig(
        {
            "quality": "high_quality",
            "disable_caching": True,
            "custom_folders": True,
            "media_dir": "docs/media",
        }
    ):

        class CustomSCene(Scene):
            def construct(self):
                axes = Axes(x_range=[0, 5], y_range=[0, 1.5], x_length=6, y_length=3)
                axes.add_coordinates(None, [0, 1], None)
                size = 5
                changes = 3

                dist1 = softmax(np.random.randn(size))
                bars = ChartBars(axes, dist1, xs=list(range(size)), fill_color=PURE_BLUE)
                self.add(axes, bars)
                for i in range(changes):
                    dist2 = softmax(np.random.randn(size))
                    self.play(bars.animate.set_values(dist2), run_time=2)
                self.play(bars.animate.set_values(dist1), run_time=2)

        scene = CustomSCene()
        scene.render()
