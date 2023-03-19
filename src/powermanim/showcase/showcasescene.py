import abc
from typing import Type

from manim import *


class ShowcaseMeta(abc.ABCMeta):
    showcase_scenes = []

    def __new__(cls, clsname, bases, attrs):
        newclass = super().__new__(cls, clsname, bases, attrs)
        if clsname != "ShowcaseScene":
            cls.showcase_scenes.append(newclass)
        return newclass


class ShowcaseScene(Scene, metaclass=ShowcaseMeta):
    @property
    @abc.abstractmethod
    def showcasing(self) -> Type[Scene]:
        pass
