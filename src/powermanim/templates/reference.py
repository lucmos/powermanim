from manim import *


class Reference(VGroup):
    def __init__(self, text: str, font_size: int = 28, color: ManimColor = LIGHT_GREY):
        text = rf"\textit{{{text}}}"
        boxtext = rf"\mbox{{{text}}}"
        tex = Tex(
            boxtext,
            font_size=font_size,
            color=color,
        ).to_corner(DL, buff=MED_SMALL_BUFF)
        super().__init__(tex)
