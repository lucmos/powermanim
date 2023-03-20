from manim import *


class NumberSlider(VGroup):
    def __init__(
        self,
        x_range=[-2, 2, 0.5],
        length=2,
    ):
        """A class to represent a number together with an associated slider.

        Args:
            x_range (list): A list of 3 floats representing x_min, x_max and x_step.
            length (float): Length of the line.
        """
        self.tracker = ValueTracker(0)

        decimal_number = DecimalNumber(self.tracker.get_value(), num_decimal_places=1)

        number_line = NumberLine(
            x_range=x_range,
            length=length,
            rotation=90 * DEGREES,
        )

        arrow = Arrow(RIGHT / 2, LEFT / 2, buff=0).next_to(number_line.n2p(self.tracker.get_value()), RIGHT)

        arrow.add_updater(lambda obj: obj.become(obj.copy().next_to(number_line.n2p(self.tracker.get_value()), RIGHT)))
        decimal_number.add_updater(
            lambda obj: obj.set_value(
                self.tracker.get_value(),
            ).next_to(number_line, LEFT, buff=MED_LARGE_BUFF)
        )

        super().__init__(decimal_number, number_line, arrow)
