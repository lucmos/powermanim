import typing as T

from manim import *


class ArrangedBulletList(VGroup):
    def __init__(
        self,
        *rows: T.Union[Tex, Text],
        line_spacing: float = MED_LARGE_BUFF * 1.5,
        left_buff: float = MED_LARGE_BUFF * 1.5,
        shift: float = 0.0,
    ):
        """A VGroup that arranges the rows in a list of bullet points.

        Args:
            rows: A list of items to be displayed.
            line_spacing: The spacing between the rows.
            left_buff: The spacing between the left edge of the rows and the left edge of the screen.
            shift: The shift of the rows.
        """
        g_rows = (
            VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=line_spacing).to_edge(LEFT, buff=left_buff).shift(shift)
        )

        super().__init__(*g_rows)
