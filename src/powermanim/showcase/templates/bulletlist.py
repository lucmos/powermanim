from manim import *

from powermanim import Bullet, BulletList
from powermanim.showcase.showcasescene import ShowcaseScene


class BulletListShowcase(ShowcaseScene):
    def showcasing():
        return BulletList

    def construct(self):
        rows = [
            Bullet("First row", group=0),
            Bullet("Second row", group=1),
            Bullet("Elements:", group=2),
            Bullet("First element", level=1, symbol="(1)", group=2),
            Bullet("Second element", level=1, symbol="(2)", group=3),
            Bullet("Third element", level=1, symbol="(3)", group=4),
        ]
        VGroup(*rows).set_opacity(0.5).scale(0.8)

        bullets = BulletList(
            *rows,
            scale_active=1.2,
        )
        self.add(bullets)

        self.play(bullets.also_next())
        self.play(bullets.also_next())
        self.play(bullets.also_next())
        self.play(bullets.also_next())
        self.play(bullets.also_next())
        self.play(bullets.clear())
        self.play(bullets.only_next())
        self.play(bullets.only_next())
        self.play(bullets.only_next())
        self.play(bullets.only_next())
        self.play(bullets.only_next())
        self.play(bullets.clear())
        self.wait()
