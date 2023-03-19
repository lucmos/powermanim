from manim import *

from powermanim.showcase.showcasescene import ShowcaseMeta

WOWCHEMY_FOLDER = "docs/static/uploads/media"
SHOWCASE_QUALITY = "medium_quality"


def test_and_gen_showcases():
    for scene in ShowcaseMeta.showcase_scenes:
        with tempconfig(
            {
                "quality": SHOWCASE_QUALITY,
                "disable_caching": True,
                "custom_folders": True,
                "media_dir": WOWCHEMY_FOLDER,
            }
        ):
            scene = scene()
            scene.render()
