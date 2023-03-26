from manim import *

from powermanim.layouts.arrangedbullets import Bullet
from powermanim.showcase.showcasescene import ShowcaseScene
from powermanim.templates.bulletlist import BulletList


class BulletListShowcase(ShowcaseScene):
    def showcasing():
        return BulletList

    def construct(self):
        rows = [
            Bullet(Text("First row"), group=0),
            Bullet(Text("Second row"), group=1),
            Bullet(Text("Elements:"), group=2),
            Bullet(Text("First element"), level=1, symbol="(1)", group=3),
            Bullet(Text("Second element"), level=1, symbol="(2)", group=4),
            Bullet(Text("Third element"), level=1, symbol="(3)", group=5),
        ]
        VGroup(*rows).set_opacity(0.5).scale(0.8)

        bullets = BulletList(
            *rows,
            scale_active=1.2,
        )
        self.add(bullets)

        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.also_next(self)
        bullets.clear(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.only_next(self)
        bullets.clear(self)
        self.wait()
