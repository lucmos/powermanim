from manim import *

from powermanim.showcase.showcasescene import ShowcaseScene
from powermanim.templates.reference import Reference


class ReferenceShowcase(ShowcaseScene):
    def showcasing():
        return Reference

    def construct(self):
        text = (
            r"Moschella et al. “Relative representations enable zero-shot latent space communication”, ICLR 2023 (oral)"
        )
        tex = Tex(text).scale(0.5)
        reference = Reference(text=text)

        self.add(tex)

        self.play(
            Transform(tex, reference[0]),
            rate_func=there_and_back_with_pause,
            run_time=3,
        )
