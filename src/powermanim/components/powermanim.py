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

        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)

        square = Difference(square, circle, color=logo_blue, fill_opacity=1)
        triangle = Difference(triangle, square, color=logo_red, fill_opacity=1)

        circle.shift(DL * self.gap)
        triangle.shift(DR * self.gap)

        return VGroup(circle, square, triangle)

    def build_text(self):
        ds_m = MathTex(r"\mathbb{PM}", fill_color=self.logo_black).scale(5)
        ds_m.shift(4.25 * LEFT + 1.5 * UP)
        return ds_m

    def build_banner(self):
        shapes = self.build_shapes()

        ds_p = MathTex(r"\mathbb{P}", fill_color=self.logo_black).scale(2)
        ower = Tex("ower", tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(2)
        ower.next_to(ds_p, RIGHT, buff=SMALL_BUFF).align_to(ds_p, DOWN).set_color(self.font_color)
        power = VGroup(ds_p, ower)

        ds_m = MathTex(r"\mathbb{M}", fill_color=self.logo_black).scale(2)
        anim = Tex("anim", tex_template=TexFontTemplates.gnu_freeserif_freesans).scale(2)
        anim.next_to(ds_m, RIGHT, buff=SMALL_BUFF).align_to(ds_m, DOWN).set_color(self.font_color)
        tmanim = VGroup(ds_m, anim)

        banner = VGroup(power, tmanim).arrange(RIGHT, buff=MED_SMALL_BUFF).move_to(ORIGIN).scale(1.5)
        banner.next_to(shapes[1], LEFT)
        banner.align_to(shapes[0].get_critical_point(UP) + self.gap, DOWN)

        return VGroup(shapes, banner).move_to(ORIGIN)

    def __init__(self, font_color="#343434", logo_black="#343434", gap=0.4):
        self.font_color = font_color
        self.logo_black = logo_black
        self.gap = gap

        shapes = self.build_shapes()
        ds_m = self.build_text()
        super().__init__(*shapes, ds_m)
        self.move_to(ORIGIN)
