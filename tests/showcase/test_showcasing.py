from manim import *

from powermanim.showcase.showcasescene import QUALITY, WOWCHEMY_FOLDER, ShowcaseMeta


def test_and_gen_showcases():
    for scene in ShowcaseMeta.showcase_scenes:
        with tempconfig(
            {
                "quality": QUALITY,
                "disable_caching": True,
                "custom_folders": True,
                "media_dir": WOWCHEMY_FOLDER,
            }
        ):
            scene = scene()
            scene.render()
