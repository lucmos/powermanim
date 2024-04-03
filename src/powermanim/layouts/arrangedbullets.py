import typing as T

from manim import *


class MathBullet(MathTex):
    def __init__(
        self,
        *text: str,
        level: int = 0,
        group: T.Optional[int] = None,
        adjustment: T.Optional[T.Union[float, T.Sequence[float]]] = 0.0,
        symbol: T.Optional[str] = r"\bullet",
        autoplace: bool = True,
        **kwargs,
    ):
        """A class to represent a bullet point.

        Args:
            text: The text to be displayed.
            level: The indent level of the bullet point.
            group: The group the bullet point belongs to, controls the animations.
            adjustment: The adjustment of the bullet.
            symbol: The symbol to be displayed as the bullet.
            autoplace: Whether to automatically place the bullet point.
        """
        self.level = level
        self.adjustment = adjustment
        self.group = group
        self.symbol = symbol
        self.autoplace = autoplace

        first_text, *rest_text = text
        if symbol is not None:
            first_text = rf"{symbol}~{first_text}"

        super().__init__(first_text, *rest_text, **kwargs)

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

    def adjust(self, adjustment: T.Optional[T.Union[float, T.Sequence[float]]] = None):
        """Adjust the bullet point.

        Args:
            adjustment: The shift of the bullet.
        """
        if adjustment is None:
            adjustment = self.adjustment
        self.shift(self.adjustment)


class Bullet(MathBullet):
    def __init__(
        self,
        *text: str,
        level: int = 0,
        group: T.Optional[int] = None,
        adjustment: T.Optional[T.Union[float, T.Sequence[float]]] = 0.0,
        symbol: T.Optional[str] = r"$\bullet$",
        force_inline: bool = False,
        arg_separator="",
        tex_environment="center",
        **kwargs,
    ):
        first_text, *rest_text = text
        if force_inline:
            first_text = r"\mbox{" + first_text
            rest_text = *rest_text, r"}"

        super().__init__(
            first_text,
            *rest_text,
            level=level,
            group=group,
            adjustment=adjustment,
            symbol=symbol,
            arg_separator=arg_separator,
            tex_environment=tex_environment,
            **kwargs,
        )


class ArrangedBullets(VGroup):
    def arrange_rows(self, rows: T.Iterable[MathBullet]):
        reference_row, *remaining_rows = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0)

        remaining_rows: T.Sequence[MathBullet]
        for bullet in remaining_rows:
            current_spacing = self.line_spacing * (self.line_spacing_decay**bullet.level)

            current_center = bullet.get_center()
            current_up = bullet.get_critical_point(UP)
            reference_down = reference_row.get_critical_point(DOWN)

            bullet.move_to(
                np.asarray(
                    [
                        # Start from the bottom of the previous line
                        # Add the decayed line spacing, depending on the bullet level
                        # Add half the object height, to account for multilines
                        current_center[0],
                        reference_down[1] - current_spacing - abs(current_center[1] - current_up[1]),
                        current_center[2],
                    ]
                )
            )
            reference_row = bullet

        for row in rows:
            row.indent(indent_buff=self.indent_buff)
            row.adjust()

    def __init__(
        self,
        *rows: T.Union[MathBullet, Bullet, MathTex, Tex, Text, str],
        line_spacing: float = MED_LARGE_BUFF * 1.5,
        line_spacing_decay: float = 1.0,
        indent_buff: float = MED_LARGE_BUFF * 1.5,
        left_buff: float = MED_LARGE_BUFF * 2,
    ):  # TODO: remove argument defaults in next version?
        """A VGroup that arranges the rows in a list of bullet points.

        Args:
            rows: A list of items to be displayed.
            line_spacing: The spacing between the rows.
            line_spacing_decay: The rate at which the spacing decays at each level
            indent_buff: The spacing between the bullet and the text.
            left_buff: The buff from the left edge
        """
        self.line_spacing = line_spacing
        self.line_spacing_decay = line_spacing_decay
        self.indent_buff = indent_buff
        self.left_buff = left_buff

        rows: T.Sequence[T.Union[MathBullet, Bullet, MathTex, Tex, Text]] = [
            (Bullet(row) if isinstance(row, str) else row) for row in rows
        ]

        self.arrange_rows([row for row in rows if row.autoplace])
        super().__init__(*rows)
        self.move_to(ORIGIN).to_edge(LEFT, self.left_buff)
