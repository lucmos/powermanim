import typing as T

from manim import *

from powermanim.components.vgrouphighlight import VGroupHighlight
from powermanim.layouts.arrangedbulletlist import ArrangedBulletList


class BulletList(VGroup):
    def __init__(
        self,
        *rows: T.Union[Tex, Text],
        line_spacing: float = MED_LARGE_BUFF * 1.5,
        left_buff: float = MED_LARGE_BUFF * 2,
        shift: float = 0.0,
        inactive_opacity: float = 0.5,
        active_opacity: float = 1.0,
        scale_active: float = 1.0,
    ):
        """A class to represent an highlatable list of items.

        Args:
            rows: A list of items to be displayed.
            line_spacing: The spacing between the rows.
            left_buff: The spacing between the left edge of the rows and the left edge of the screen.
            shift: The shift to apply to the rows.
            inactive_opacity: The opacity of the inactive items.
            active_opacity: The opacity of the active items.
            scale_active: The scale of the active items.
        """
        ArrangedBulletList(
            *rows,
            line_spacing=line_spacing,
            left_buff=left_buff,
            shift=shift,
        ).set_opacity(inactive_opacity)

        self.rows = VGroupHighlight(
            *rows,
            active_opacity=active_opacity,
            scale_active=scale_active,
            scale_about_edge=LEFT,
        )
        super().__init__(self.rows)

        self.highlighted = 0

    def also_next(self, scene: Scene) -> None:
        """Highlights also the next item in the list."""
        self.highlighted += 1

        self.rows.highlight(scene=scene, indices=list(range(self.highlighted)))

    def only_next(self, scene: Scene) -> None:
        """Highlights only the next item in the list."""
        self.rows.highlight(scene=scene, indices=self.highlighted)
        self.highlighted += 1

    def clear(self, scene: Scene) -> None:
        """Clears the list hightlighting."""
        self.rows.highlight(scene=scene, indices=[])
        self.highlighted = 0

    def all(self, scene: Scene) -> None:
        """Highlights all the list."""
        self.rows.highlight(scene=scene, indices=list(range(len(self.rows))))
