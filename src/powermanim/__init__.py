from .components import (
    ChartBars,
    DirectionalArrow,
    GroupActivable,
    Invariance,
    NumberSlider,
    PowerManim,
    VActivable,
    VAutoActivable,
)
from .layouts import ArrangedBullets, Bullet, MathBullet, SwitchPalette
from .templates import BulletList, Reference, SectionTitle

__all__ = [
    "VAutoActivable",
    "ChartBars",
    "DirectionalArrow",
    "VActivable",
    "Invariance",
    "NumberSlider",
    "PowerManim",
    "GroupActivable",
    "ArrangedBullets",
    "SwitchPalette",
    "Bullet",
    "BulletList",
    "MathBullet",
    "Reference",
    "SectionTitle",
]

try:
    from ._version import __version__ as __version__
except ImportError:
    import sys

    print(
        "Project not installed in the current env, activate the correct env or install it with:\n\tpip install -e .",
        file=sys.stderr,
    )
    __version__ = "unknown"
