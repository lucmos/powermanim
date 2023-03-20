import abc
from typing import Any, Sequence, Type

from manim import *

# The path to the folder where the animations are stored.
WOWCHEMY_FOLDER = "docs/static/uploads/media"

# The selected quality of the animations to display in the website
QUALITY = "medium_quality"

# The mapping between the quality and the resolution of the animations.
QUALITY2RES = {
    "high_quality": "1080p60",
    "medium_quality": "720p30",
    "low_quality": "480p15",
}


class ShowcaseMeta(abc.ABCMeta):
    """Metaclass for ShowcaseScene.

    This metaclass is used to register all ShowcaseScene subclasses in the
    showcase_scenes attribute.
    """

    showcase_scenes: Sequence[Type[Scene]] = []

    def __new__(cls, clsname, bases, attrs):
        newclass = super().__new__(cls, clsname, bases, attrs)
        if clsname != "ShowcaseScene":
            cls.showcase_scenes.append(newclass)
        return newclass


class ShowcaseScene(Scene, metaclass=ShowcaseMeta):
    """Abstract class that all showcase scene must extend."""

    @staticmethod
    @abc.abstractmethod
    def showcasing(self) -> Type[Any]:
        """The component this showcase is showcasing.

        All showcase scenes must implement this method.

        Returns:
            The object being showcased by this scene.
        """
        pass
