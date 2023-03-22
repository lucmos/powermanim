from manim import *

from powermanim.showcase.showcasescene import ShowcaseScene
from powermanim.templates.bulletlist import BulletList


class BulletListShowcase(ShowcaseScene):
    def showcasing():
        return BulletList

    def construct(self):
        rows = [
            Text(row)
            for row in [
                "First row",
                "Second row",
                "Third row",
                "Fourth row",
            ]
        ]
        grouped_rows = (
            VGroup(*rows)
            .arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF * 1.5)
            .to_edge(LEFT, buff=MED_LARGE_BUFF * 1.5)
        )
        grouped_rows.set_opacity(0.5).scale(0.8)

        bullets = BulletList(
            *rows,
            scale_active=1.2,
        )
        self.add(bullets)

        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.clear(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.clear(self)
        self.wait()
