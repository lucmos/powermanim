from manim import *
from manim.utils.color import Color


class SectionTitle(VGroup):
    def __init__(
        self,
        section_title: str,
        in_run_time: float = 0.75,
        out_run_time: float = 0.25,
        out_shift: float = UP,
        border_color: Color = BLUE,
        border_buff: float = MED_LARGE_BUFF,
        border_lag_ratio: float = 0.5,
    ):
        """Section title transition.

        Args:
            section_title (str): Title of the section
            in_run_time (float, optional): Run time of the animation. Defaults to 0.75.
            out_run_time (float, optional): Run time of the animation. Defaults to 0.25.
            out_shift (float, optional): Shift of the animation. Defaults to UP.
            border_color (Color, optional): Color of the border. Defaults to BLUE.
            border_buff (float, optional): Buffer of the border. Defaults to MED_LARGE_BUFF.
            border_lag_ratio (float, optional): Lag ratio of the border. Defaults to 0.5.
        """
        self.slide_title = Tex(section_title, font_size=72)
        self.border_color = border_color
        self.border_buff = border_buff
        self.border_lag_ratio = border_lag_ratio
        self.in_run_time = in_run_time
        self.out_run_time = out_run_time
        self.out_shift = out_shift

        super().__init__(self.slide_title)

    def show(self, scene: Scene) -> None:
        """Show the section title.

        Args:
            scene (Scene): the scene.
        """
        scene.play(
            AnimationGroup(
                DrawBorderThenFill(self.slide_title, run_time=self.in_run_time),
                Circumscribe(
                    self.slide_title,
                    color=self.border_color,
                    buff=self.border_buff,
                ),
                lag_ratio=self.border_lag_ratio,
            )
        )

    def hide(self, scene: Scene) -> None:
        """Hide the section title.

        Args:
            scene (Scene): the scene.
        """
        scene.play(
            FadeOut(self.slide_title, shift=self.out_shift),
            run_time=self.out_run_time,
        )
