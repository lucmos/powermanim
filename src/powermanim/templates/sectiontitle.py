from manim import *


class SectionTitle(VGroup):
    def __init__(
        self,
        section_title: str,
    ):
        """Section title transition.

        Args:
            section_title: Title of the section
        """
        self.slide_title = Tex(section_title, font_size=72)
        super().__init__(self.slide_title)

    def show(self, scene: Scene) -> None:
        """Show the section title.

        Args:
            scene (Scene): the scene.
        """
        scene.play(
            AnimationGroup(
                DrawBorderThenFill(self.slide_title, run_time=0.75),
                Circumscribe(
                    self.slide_title,
                    color=BLUE,
                    buff=MED_LARGE_BUFF,
                ),
                lag_ratio=0.5,
            )
        )

    def hide(self, scene: Scene) -> None:
        """Hide the section title.

        Args:
            scene (Scene): the scene.
        """
        scene.play(
            FadeOut(self.slide_title, shift=UP),
            run_time=0.25,
        )
