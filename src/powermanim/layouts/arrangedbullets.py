import typing as T
from collections import defaultdict

from manim import *


class Bullet(VGroup):
    def __init__(
        self,
        *text: T.Union[Tex, Text, MathTex],
        level: int = 0,
        group: T.Optional[int] = None,
        adjustment: float = 0.0,
        symbol: T.Optional[str] = r"$\bullet$",
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        text_components_buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    ):
        """A class to represent a bullet point.

        Args:
            text: The text to be displayed.
            level: The indent level of the bullet point.
            group: The group the bullet point belongs to, controls the animations.
            adjustment: The adjustment of the bullet.
            symbol: The symbol to be displayed as the bullet.
            buff: The spacing between the bullet and the text.
            text_components_buff: The spacing between the text components.
        """
        self.level = level
        self.adjustment = adjustment
        self.group = group

        self.text = VGroup(*text).arrange(RIGHT, buff=text_components_buff)
        self.bullet = symbol

        if symbol is not None:
            self.bullet = Tex(symbol)
            self.bullet.next_to(self.text, LEFT, buff=buff)
        super().__init__(VGroup(self.bullet, self.text) if self.bullet is not None else self.text)

    def indent(self, indent_buff: float = MED_LARGE_BUFF * 1.5):
        """Indent the bullet point.

        Args:
            indent_buff: The spacing between the bullet and the text.
        """
        self.shift(RIGHT * indent_buff * self.level)

    def unindent(self, indent_buff: float = MED_LARGE_BUFF * 1.5):
        """Unindent the bullet point.

        Args:
            indent_buff: The spacing between the bullet and the text.
        """
        self.shift(LEFT * indent_buff * self.intend_level)

    def adjust(self, adjustment: T.Optional[float] = None):
        """Adjust the bullet point.

        Args:
            adjustment: The shift of the bullet.
        """
        if adjustment is None:
            adjustment = self.adjustment
        self.shift(self.adjustment)


class ArrangedBullets(VGroup):
    def __init__(
        self,
        *rows: T.Union[Bullet, MathTex, Tex, Text],
        line_spacing: float = MED_LARGE_BUFF * 1.5,
        indent_buff: float = MED_LARGE_BUFF * 1.5,
        left_buff: float = MED_LARGE_BUFF * 1.5,
        global_shift: float = 0.0,
    ):
        """A VGroup that arranges the rows in a list of bullet points.

        Args:
            rows: A list of items to be displayed.
            line_spacing: The spacing between the rows.
            indent_buff: The spacing between the bullet and the text.
            left_buff: The spacing between the left edge of the rows and the left edge of the screen.
            global_shift: The global_shift of the rows.
        """
        self.line_spacing = line_spacing
        self.indent_buff = indent_buff
        self.left_buff = left_buff
        self.global_shift = global_shift

        rows = [(row if isinstance(row, Bullet) else Bullet(row)) for row in rows]
        bullet_rows: T.Iterable[Bullet] = (
            VGroup(*rows)
            .arrange(DOWN, aligned_edge=LEFT, buff=line_spacing)
            .to_edge(LEFT, buff=left_buff)
            .shift(global_shift)
        )

        for row in bullet_rows:
            row.indent(indent_buff=indent_buff)
            row.adjust()

        groups = [row.group for row in bullet_rows]

        # If there is a None and aso something else
        if (None in groups) and len(set(groups)) != 1:
            raise ValueError("The groups must be specified for all or no bullets at all.")

        if None in groups:
            groups = list(range(len(bullet_rows)))

        group2bullet = defaultdict(list)
        for i, row in enumerate(bullet_rows):
            group = row.group
            if group is None:
                group = i
            group2bullet[group].append(row)

        group_rows = []
        for _, bullets in group2bullet.items():
            group_rows.append(VGroup(*bullets))

        super().__init__(*group_rows)
        self.ngroups = len(self)
