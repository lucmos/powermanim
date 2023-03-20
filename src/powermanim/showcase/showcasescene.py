import abc
from typing import Any, Sequence, Type

from manim import *

WOWCHEMY_FOLDER = "docs/static/uploads/media"
QUALITY = "medium_quality"
QUALITY2RES = {
    "high_quality": "1080p60",
    "medium_quality": "720p30",
    "low_quality": "480p15",
}


class ShowcaseMeta(abc.ABCMeta):
    showcase_scenes: Sequence[Type[Scene]] = []

    def __new__(cls, clsname, bases, attrs):
        newclass = super().__new__(cls, clsname, bases, attrs)
        if clsname != "ShowcaseScene":
            cls.showcase_scenes.append(newclass)
        return newclass


class ShowcaseScene(Scene, metaclass=ShowcaseMeta):
    @staticmethod
    @abc.abstractmethod
    def showcasing(self) -> Type[Any]:
        pass
