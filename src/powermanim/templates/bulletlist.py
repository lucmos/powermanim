import typing as T

from manim import *

from powermanim.components.vgrouphighlight import AutoHighlightable, VGroupHighlight
from powermanim.layouts.arrangedbullets import ArrangedBullets


class BulletList(VGroup):
    def __init__(
        self,
        *rows: T.Union[MathBullet, Tex, Text],
        line_spacing: float = MED_LARGE_BUFF * 1.5,
        indent_buff: float = MED_LARGE_BUFF * 1.5,
        left_buff: float = MED_LARGE_BUFF * 2,
        global_shift: float = 0.0,
        inactive_opacity: float = 0.5,
        active_opacity: float = 1.0,
        scale_active: float = 1.0,
    ):
        """A class to represent an highlatable list of items.

        Args:
            rows: A list of items to be displayed.
            line_spacing: The spacing between the rows.
            indent_buff: The spacing between the bullet and the text.
            left_buff: The spacing between the left edge of the rows and the left edge of the screen.
            global_shift: The global_shift to apply to the rows.
            inactive_opacity: The opacity of the inactive items.
            active_opacity: The opacity of the active items.
            scale_active: The scale of the active items.
        """
        self.arranged_list = ArrangedBullets(
            *rows,
            line_spacing=line_spacing,
            indent_buff=indent_buff,
            left_buff=left_buff,
            global_shift=global_shift,
        )

        self.rows = VGroupHighlight(
            *(
                AutoHighlightable(
                    x,
                    active_fill_opacity=active_opacity,
                    active_stroke_opacity=active_opacity,
                    inactive_fill_opacity=inactive_opacity,
                    inactive_stroke_opacity=inactive_opacity,
                    scale_active=scale_active,
                    scale_about_edge=LEFT,
                    group=x.group if isinstance(x, MathBullet) else None,
                )
                for x in self.arranged_list
            )
        )
        super().__init__(self.rows)

    @property
    def ngroups(self) -> int:
        return len(self.nrows)

    def also_next(self) -> Animation:
        """Highlights also the next item in the list."""
        return self.rows.also_next()

    def only_next(self) -> Animation:
        """Highlights only the next item in the list."""
        return self.rows.only_next()

    def clear(self) -> Animation:
        """Clears the list hightlighting."""
        return self.rows.clear()

    def all(self) -> Animation:
        """Highlights all the list."""
        return self.rows.all()
