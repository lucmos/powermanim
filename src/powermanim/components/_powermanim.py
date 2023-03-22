from manim import *
from manim.constants import DOWN, LEFT, ORIGIN, RIGHT, UP
from manim.mobject.geometry.arc import Circle
from manim.mobject.geometry.polygram import Square, Triangle
from manim.mobject.text.tex_mobject import MathTex, Tex
from manim.mobject.types.vectorized_mobject import VGroup
from manim.utils.tex_templates import TexFontTemplates

# config["pixel_height"] = 500  #  1080 is default
# config["pixel_width"] = 1500  # 1920 is default


class PowerManim(VGroup):
    def build_shapes(self):
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Difference(Square().shift(UP), circle, color=logo_blue, fill_opacity=1).shift(UR * 0.2)
        triangle = Difference(Triangle().shift(RIGHT), square, color=logo_red, fill_opacity=1).shift(DR * 0.2)
        return VGroup(circle, square, triangle)

    def build_text(self):
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{PM}", fill_color=logo_black).scale(5)
        ds_m.shift(4.25 * LEFT + 1.5 * UP)
        return ds_m

    def build_banner(self):
        shapes = self.build_shapes()

        font_color = "#343434"
        logo_black = "#343434"

        ds_p = MathTex(r"\mathbb{P}", fill_color=logo_black).scale(2)
        ower = Tex("ower", tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(2)
        ower.next_to(ds_p, RIGHT, buff=SMALL_BUFF).align_to(ds_p, DOWN).set_color(font_color)
        power = VGroup(ds_p, ower)

        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(2)
        anim = Tex("anim", tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(2)
        anim.next_to(ds_m, RIGHT, buff=SMALL_BUFF).align_to(ds_m, DOWN).set_color(font_color)
        tmanim = VGroup(ds_m, anim)

        banner = VGroup(power, tmanim).arrange(RIGHT, buff=MED_SMALL_BUFF).move_to(ORIGIN).scale(1.5)
        banner.shift(UP * 0.5 + LEFT * 0.5)
        shapes.next_to(banner.get_critical_point(DR), DR, buff=-1)

        return VGroup(shapes, banner).move_to(ORIGIN)

    def __init__(self):
        shapes = self.build_shapes()
        ds_m = self.build_text()
        super().__init__(*shapes, ds_m)
        self.move_to(ORIGIN)
