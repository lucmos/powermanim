from .components import (
    AutoHighlightable,
    ChartBars,
    DirectionalArrow,
    Highlightable,
    Invariance,
    NumberSlider,
    PowerManim,
    VGroupHighlight,
)
from .layouts import ArrangedBullets, Bullet, MathBullet, SwitchPalette
from .templates import BulletList, Reference, SectionTitle

__all__ = [
    "AutoHighlightable",
    "ChartBars",
    "DirectionalArrow",
    "Highlightable",
    "Invariance",
    "NumberSlider",
    "PowerManim",
    "VGroupHighlight",
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
