from __future__ import annotations

from copy import deepcopy

import manim.utils.color.manim_colors as Colors
from manim import *


class SwitchPalette:
    def __init__(self):
        self.ORIGINAL_BLACK = deepcopy(Colors.BLACK)
        self.ORIGINAL_GRAY_E = deepcopy(Colors.GRAY_E)
        self.ORIGINAL_GREY_E = deepcopy(Colors.GREY_E)
        self.ORIGINAL_GRAY_D = deepcopy(Colors.GRAY_D)
        self.ORIGINAL_GREY_D = deepcopy(Colors.GREY_D)
        self.ORIGINAL_GRAY_C = deepcopy(Colors.GRAY_C)
        self.ORIGINAL_GREY_C = deepcopy(Colors.GREY_C)
        self.ORIGINAL_GRAY_B = deepcopy(Colors.GRAY_B)
        self.ORIGINAL_GREY_B = deepcopy(Colors.GREY_B)
        self.ORIGINAL_GRAY_A = deepcopy(Colors.GRAY_A)
        self.ORIGINAL_GREY_A = deepcopy(Colors.GREY_A)
        self.ORIGINAL_WHITE = deepcopy(Colors.WHITE)
        self.ORIGINAL_DARKER_GRAY = deepcopy(Colors.DARKER_GRAY)
        self.ORIGINAL_DARKER_GREY = deepcopy(Colors.DARKER_GREY)
        self.ORIGINAL_DARK_GRAY = deepcopy(Colors.DARK_GRAY)
        self.ORIGINAL_DARK_GREY = deepcopy(Colors.DARK_GREY)
        self.ORIGINAL_GRAY = deepcopy(Colors.GRAY)
        self.ORIGINAL_GREY = deepcopy(Colors.GREY)
        self.ORIGINAL_LIGHT_GRAY = deepcopy(Colors.LIGHT_GRAY)
        self.ORIGINAL_LIGHT_GREY = deepcopy(Colors.LIGHT_GREY)
        self.ORIGINAL_LIGHTER_GRAY = deepcopy(Colors.LIGHTER_GRAY)
        self.ORIGINAL_LIGHTER_GREY = deepcopy(Colors.LIGHTER_GREY)
        self.ORIGINAL_BLUE_E = deepcopy(Colors.BLUE_E)
        self.ORIGINAL_BLUE_D = deepcopy(Colors.BLUE_D)
        self.ORIGINAL_BLUE_C = deepcopy(Colors.BLUE_C)
        self.ORIGINAL_BLUE_B = deepcopy(Colors.BLUE_B)
        self.ORIGINAL_BLUE_A = deepcopy(Colors.BLUE_A)
        self.ORIGINAL_TEAL_E = deepcopy(Colors.TEAL_E)
        self.ORIGINAL_TEAL_D = deepcopy(Colors.TEAL_D)
        self.ORIGINAL_TEAL_C = deepcopy(Colors.TEAL_C)
        self.ORIGINAL_TEAL_B = deepcopy(Colors.TEAL_B)
        self.ORIGINAL_TEAL_A = deepcopy(Colors.TEAL_A)
        self.ORIGINAL_GREEN_E = deepcopy(Colors.GREEN_E)
        self.ORIGINAL_GREEN_D = deepcopy(Colors.GREEN_D)
        self.ORIGINAL_GREEN_C = deepcopy(Colors.GREEN_C)
        self.ORIGINAL_GREEN_B = deepcopy(Colors.GREEN_B)
        self.ORIGINAL_GREEN_A = deepcopy(Colors.GREEN_A)
        self.ORIGINAL_YELLOW_E = deepcopy(Colors.YELLOW_E)
        self.ORIGINAL_YELLOW_D = deepcopy(Colors.YELLOW_D)
        self.ORIGINAL_YELLOW_C = deepcopy(Colors.YELLOW_C)
        self.ORIGINAL_YELLOW_B = deepcopy(Colors.YELLOW_B)
        self.ORIGINAL_YELLOW_A = deepcopy(Colors.YELLOW_A)
        self.ORIGINAL_GOLD_E = deepcopy(Colors.GOLD_E)
        self.ORIGINAL_GOLD_D = deepcopy(Colors.GOLD_D)
        self.ORIGINAL_GOLD_C = deepcopy(Colors.GOLD_C)
        self.ORIGINAL_GOLD_B = deepcopy(Colors.GOLD_B)
        self.ORIGINAL_GOLD_A = deepcopy(Colors.GOLD_A)
        self.ORIGINAL_RED_E = deepcopy(Colors.RED_E)
        self.ORIGINAL_RED_D = deepcopy(Colors.RED_D)
        self.ORIGINAL_RED_C = deepcopy(Colors.RED_C)
        self.ORIGINAL_RED_B = deepcopy(Colors.RED_B)
        self.ORIGINAL_RED_A = deepcopy(Colors.RED_A)
        self.ORIGINAL_MAROON_E = deepcopy(Colors.MAROON_E)
        self.ORIGINAL_MAROON_D = deepcopy(Colors.MAROON_D)
        self.ORIGINAL_MAROON_C = deepcopy(Colors.MAROON_C)
        self.ORIGINAL_MAROON_B = deepcopy(Colors.MAROON_B)
        self.ORIGINAL_MAROON_A = deepcopy(Colors.MAROON_A)
        self.ORIGINAL_PURPLE_E = deepcopy(Colors.PURPLE_E)
        self.ORIGINAL_PURPLE_D = deepcopy(Colors.PURPLE_D)
        self.ORIGINAL_PURPLE_C = deepcopy(Colors.PURPLE_C)
        self.ORIGINAL_PURPLE_B = deepcopy(Colors.PURPLE_B)
        self.ORIGINAL_PURPLE_A = deepcopy(Colors.PURPLE_A)
        self.ORIGINAL_PINK = deepcopy(Colors.PINK)
        self.ORIGINAL_LIGHT_PINK = deepcopy(Colors.LIGHT_PINK)
        self.ORIGINAL_DARK_BROWN = deepcopy(Colors.DARK_BROWN)
        self.ORIGINAL_LIGHT_BROWN = deepcopy(Colors.LIGHT_BROWN)

        self.ORIGINAL_YELLOW = deepcopy(Colors.YELLOW)

    def switch_to_white_palette(self) -> SwitchPalette:
        """Switch to white palette.

        Must be called before the scene is created, after the manim imports.

        This function is intended to be used to convert slides from the black palette to the white palette.
        Do not use it to build white slides from scratch, since it doesn't have consistent colors naming,

        e.g., after switching the palette, "BLACK" has the value of "WHITE" and "WHITE" has the value of "BLACK".
        """
        config.background_color = Colors.WHITE

        Colors.WHITE._internal_value = self.ORIGINAL_BLACK._internal_value
        Colors.GRAY_A._internal_value = self.ORIGINAL_GRAY_E._internal_value
        Colors.GREY_A._internal_value = self.ORIGINAL_GREY_E._internal_value
        Colors.GRAY_B._internal_value = self.ORIGINAL_GRAY_D._internal_value
        Colors.GREY_B._internal_value = self.ORIGINAL_GREY_D._internal_value
        Colors.GRAY_C._internal_value = self.ORIGINAL_GRAY_C._internal_value
        Colors.GREY_C._internal_value = self.ORIGINAL_GREY_C._internal_value
        Colors.GRAY_D._internal_value = self.ORIGINAL_GRAY_B._internal_value
        Colors.GREY_D._internal_value = self.ORIGINAL_GREY_B._internal_value
        Colors.GRAY_E._internal_value = self.ORIGINAL_GRAY_A._internal_value
        Colors.GREY_E._internal_value = self.ORIGINAL_GREY_A._internal_value
        Colors.BLACK._internal_value = self.ORIGINAL_WHITE._internal_value

        Colors.LIGHTER_GRAY._internal_value = self.ORIGINAL_DARKER_GRAY._internal_value
        Colors.LIGHTER_GREY._internal_value = self.ORIGINAL_DARKER_GREY._internal_value
        Colors.LIGHT_GRAY._internal_value = self.ORIGINAL_DARK_GRAY._internal_value
        Colors.LIGHT_GREY._internal_value = self.ORIGINAL_DARK_GREY._internal_value
        Colors.GRAY._internal_value = self.ORIGINAL_GRAY._internal_value
        Colors.GREY._internal_value = self.ORIGINAL_GREY._internal_value
        Colors.DARK_GRAY._internal_value = self.ORIGINAL_LIGHT_GRAY._internal_value
        Colors.DARK_GREY._internal_value = self.ORIGINAL_LIGHT_GREY._internal_value
        Colors.DARKER_GRAY._internal_value = self.ORIGINAL_LIGHTER_GRAY._internal_value
        Colors.DARKER_GREY._internal_value = self.ORIGINAL_LIGHTER_GREY._internal_value

        Colors.BLUE_A._internal_value = self.ORIGINAL_BLUE_E._internal_value
        Colors.BLUE_B._internal_value = self.ORIGINAL_BLUE_D._internal_value
        Colors.BLUE_C._internal_value = self.ORIGINAL_BLUE_C._internal_value
        Colors.BLUE_D._internal_value = self.ORIGINAL_BLUE_B._internal_value
        Colors.BLUE_E._internal_value = self.ORIGINAL_BLUE_A._internal_value

        Colors.TEAL_A._internal_value = self.ORIGINAL_TEAL_E._internal_value
        Colors.TEAL_B._internal_value = self.ORIGINAL_TEAL_D._internal_value
        Colors.TEAL_C._internal_value = self.ORIGINAL_TEAL_C._internal_value
        Colors.TEAL_D._internal_value = self.ORIGINAL_TEAL_B._internal_value
        Colors.TEAL_E._internal_value = self.ORIGINAL_TEAL_A._internal_value

        Colors.GREEN_A._internal_value = self.ORIGINAL_GREEN_E._internal_value
        Colors.GREEN_B._internal_value = self.ORIGINAL_GREEN_D._internal_value
        Colors.GREEN_C._internal_value = self.ORIGINAL_GREEN_C._internal_value
        Colors.GREEN_D._internal_value = self.ORIGINAL_GREEN_B._internal_value
        Colors.GREEN_E._internal_value = self.ORIGINAL_GREEN_A._internal_value

        Colors.YELLOW_A._internal_value = self.ORIGINAL_YELLOW_E._internal_value
        Colors.YELLOW_B._internal_value = self.ORIGINAL_YELLOW_D._internal_value
        Colors.YELLOW_C._internal_value = self.ORIGINAL_YELLOW_C._internal_value
        Colors.YELLOW_D._internal_value = self.ORIGINAL_YELLOW_B._internal_value
        Colors.YELLOW_E._internal_value = self.ORIGINAL_YELLOW_A._internal_value

        Colors.GOLD_A._internal_value = self.ORIGINAL_GOLD_E._internal_value
        Colors.GOLD_B._internal_value = self.ORIGINAL_GOLD_D._internal_value
        Colors.GOLD_C._internal_value = self.ORIGINAL_GOLD_C._internal_value
        Colors.GOLD_D._internal_value = self.ORIGINAL_GOLD_B._internal_value
        Colors.GOLD_E._internal_value = self.ORIGINAL_GOLD_A._internal_value

        Colors.RED_A._internal_value = self.ORIGINAL_RED_E._internal_value
        Colors.RED_B._internal_value = self.ORIGINAL_RED_D._internal_value
        Colors.RED_C._internal_value = self.ORIGINAL_RED_C._internal_value
        Colors.RED_D._internal_value = self.ORIGINAL_RED_B._internal_value
        Colors.RED_E._internal_value = self.ORIGINAL_RED_A._internal_value

        Colors.MAROON_A._internal_value = self.ORIGINAL_MAROON_E._internal_value
        Colors.MAROON_B._internal_value = self.ORIGINAL_MAROON_D._internal_value
        Colors.MAROON_C._internal_value = self.ORIGINAL_MAROON_C._internal_value
        Colors.MAROON_D._internal_value = self.ORIGINAL_MAROON_B._internal_value
        Colors.MAROON_E._internal_value = self.ORIGINAL_MAROON_A._internal_value

        Colors.PURPLE_A._internal_value = self.ORIGINAL_PURPLE_E._internal_value
        Colors.PURPLE_B._internal_value = self.ORIGINAL_PURPLE_D._internal_value
        Colors.PURPLE_C._internal_value = self.ORIGINAL_PURPLE_C._internal_value
        Colors.PURPLE_D._internal_value = self.ORIGINAL_PURPLE_B._internal_value
        Colors.PURPLE_E._internal_value = self.ORIGINAL_PURPLE_A._internal_value

        Colors.LIGHT_BROWN._internal_value = self.ORIGINAL_DARK_BROWN._internal_value
        Colors.DARK_BROWN._internal_value = self.ORIGINAL_LIGHT_BROWN._internal_value

        Colors.PINK._internal_value = self.ORIGINAL_LIGHT_PINK._internal_value
        Colors.LIGHT_PINK._internal_value = self.ORIGINAL_PINK._internal_value

        # Fix the yellow color
        Colors.YELLOW._internal_value = ManimColor._internal_from_hex_string("F8DB5F", alpha=1)
        Colors.YELLOW_C._internal_value = ManimColor._internal_from_hex_string("F8DB5F", alpha=1)
        return self

    def restore_palette(self) -> SwitchPalette:
        """Switch to the original manim palette."""
        # Restore the original palette
        Colors.WHITE._internal_value = self.ORIGINAL_WHITE._internal_value
        Colors.GRAY_A._internal_value = self.ORIGINAL_GRAY_A._internal_value
        Colors.GREY_A._internal_value = self.ORIGINAL_GREY_A._internal_value
        Colors.GRAY_B._internal_value = self.ORIGINAL_GRAY_B._internal_value
        Colors.GREY_B._internal_value = self.ORIGINAL_GREY_B._internal_value
        Colors.GRAY_C._internal_value = self.ORIGINAL_GRAY_C._internal_value
        Colors.GREY_C._internal_value = self.ORIGINAL_GREY_C._internal_value
        Colors.GRAY_D._internal_value = self.ORIGINAL_GRAY_D._internal_value
        Colors.GREY_D._internal_value = self.ORIGINAL_GREY_D._internal_value
        Colors.GRAY_E._internal_value = self.ORIGINAL_GRAY_E._internal_value
        Colors.GREY_E._internal_value = self.ORIGINAL_GREY_E._internal_value
        Colors.BLACK._internal_value = self.ORIGINAL_BLACK._internal_value

        Colors.LIGHTER_GRAY._internal_value = self.ORIGINAL_LIGHTER_GRAY._internal_value
        Colors.LIGHTER_GREY._internal_value = self.ORIGINAL_LIGHTER_GREY._internal_value
        Colors.LIGHT_GRAY._internal_value = self.ORIGINAL_LIGHT_GRAY._internal_value
        Colors.LIGHT_GREY._internal_value = self.ORIGINAL_LIGHT_GREY._internal_value
        Colors.GRAY._internal_value = self.ORIGINAL_GRAY._internal_value
        Colors.GREY._internal_value = self.ORIGINAL_GREY._internal_value
        Colors.DARK_GRAY._internal_value = self.ORIGINAL_DARK_GRAY._internal_value
        Colors.DARK_GREY._internal_value = self.ORIGINAL_DARK_GREY._internal_value
        Colors.DARKER_GRAY._internal_value = self.ORIGINAL_DARKER_GRAY._internal_value
        Colors.DARKER_GREY._internal_value = self.ORIGINAL_DARKER_GREY._internal_value

        Colors.BLUE_A._internal_value = self.ORIGINAL_BLUE_A._internal_value
        Colors.BLUE_B._internal_value = self.ORIGINAL_BLUE_B._internal_value
        Colors.BLUE_C._internal_value = self.ORIGINAL_BLUE_C._internal_value
        Colors.BLUE_D._internal_value = self.ORIGINAL_BLUE_D._internal_value
        Colors.BLUE_E._internal_value = self.ORIGINAL_BLUE_E._internal_value

        Colors.TEAL_A._internal_value = self.ORIGINAL_TEAL_A._internal_value
        Colors.TEAL_B._internal_value = self.ORIGINAL_TEAL_B._internal_value
        Colors.TEAL_C._internal_value = self.ORIGINAL_TEAL_C._internal_value
        Colors.TEAL_D._internal_value = self.ORIGINAL_TEAL_D._internal_value
        Colors.TEAL_E._internal_value = self.ORIGINAL_TEAL_E._internal_value

        Colors.GREEN_A._internal_value = self.ORIGINAL_GREEN_A._internal_value
        Colors.GREEN_B._internal_value = self.ORIGINAL_GREEN_B._internal_value
        Colors.GREEN_C._internal_value = self.ORIGINAL_GREEN_C._internal_value
        Colors.GREEN_D._internal_value = self.ORIGINAL_GREEN_D._internal_value
        Colors.GREEN_E._internal_value = self.ORIGINAL_GREEN_E._internal_value

        Colors.YELLOW_A._internal_value = self.ORIGINAL_YELLOW_A._internal_value
        Colors.YELLOW_B._internal_value = self.ORIGINAL_YELLOW_B._internal_value
        Colors.YELLOW_C._internal_value = self.ORIGINAL_YELLOW_C._internal_value
        Colors.YELLOW_D._internal_value = self.ORIGINAL_YELLOW_D._internal_value
        Colors.YELLOW_E._internal_value = self.ORIGINAL_YELLOW_E._internal_value

        Colors.GOLD_A._internal_value = self.ORIGINAL_GOLD_A._internal_value
        Colors.GOLD_B._internal_value = self.ORIGINAL_GOLD_B._internal_value
        Colors.GOLD_C._internal_value = self.ORIGINAL_GOLD_C._internal_value
        Colors.GOLD_D._internal_value = self.ORIGINAL_GOLD_D._internal_value
        Colors.GOLD_E._internal_value = self.ORIGINAL_GOLD_E._internal_value

        Colors.RED_A._internal_value = self.ORIGINAL_RED_A._internal_value
        Colors.RED_B._internal_value = self.ORIGINAL_RED_B._internal_value
        Colors.RED_C._internal_value = self.ORIGINAL_RED_C._internal_value
        Colors.RED_D._internal_value = self.ORIGINAL_RED_D._internal_value
        Colors.RED_E._internal_value = self.ORIGINAL_RED_E._internal_value

        Colors.MAROON_A._internal_value = self.ORIGINAL_MAROON_A._internal_value
        Colors.MAROON_B._internal_value = self.ORIGINAL_MAROON_B._internal_value
        Colors.MAROON_C._internal_value = self.ORIGINAL_MAROON_C._internal_value
        Colors.MAROON_D._internal_value = self.ORIGINAL_MAROON_D._internal_value
        Colors.MAROON_E._internal_value = self.ORIGINAL_MAROON_E._internal_value

        Colors.PURPLE_A._internal_value = self.ORIGINAL_PURPLE_A._internal_value
        Colors.PURPLE_B._internal_value = self.ORIGINAL_PURPLE_B._internal_value
        Colors.PURPLE_C._internal_value = self.ORIGINAL_PURPLE_C._internal_value
        Colors.PURPLE_D._internal_value = self.ORIGINAL_PURPLE_D._internal_value
        Colors.PURPLE_E._internal_value = self.ORIGINAL_PURPLE_E._internal_value

        Colors.LIGHT_BROWN._internal_value = self.ORIGINAL_LIGHT_BROWN._internal_value
        Colors.DARK_BROWN._internal_value = self.ORIGINAL_DARK_BROWN._internal_value

        Colors.PINK._internal_value = self.ORIGINAL_PINK._internal_value
        Colors.LIGHT_PINK._internal_value = self.ORIGINAL_LIGHT_PINK._internal_value

        # Restore the yellow color
        Colors.YELLOW._internal_value = self.ORIGINAL_YELLOW._internal_value

        config.background_color = Colors.BLACK

        return self
