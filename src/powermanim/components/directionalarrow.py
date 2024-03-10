import typing as tp

from manim import *


class DirectionalArrow(Arrow):
    def __init__(
        self,
        start: tp.Union[VMobject, np.ndarray],
        end: tp.Union[VMobject, np.ndarray],
        direction: tp.Optional[np.ndarray] = None,
        stroke_width: float = 6,
        buff: float = MED_SMALL_BUFF,
        max_tip_length_to_length_ratio: float = 0.25,
        max_stroke_width_to_length_ratio: float = 5,
        **kwargs,
    ) -> None:
        """Create an arrow between two points with a given forced direction.

        If the direction is not given, it will be estimated from the start and end points.

        Args:
            start (tp.Union[VMobject, np.ndarray]): The start point of the arrow.
            end (tp.Union[VMobject, np.ndarray]): The end point of the arrow.
            direction (tp.Optional[np.ndarray], optional): The forced direction of the arrow. Defaults to None.
            stroke_width (float, optional): The width of the arrow. Defaults to 6.
            buff (float, optional): The buffer between the start and end points. Defaults to MED_SMALL_BUFF.
            max_tip_length_to_length_ratio (float, optional): The maximum tip length to length ratio. Defaults to 0.25.
            max_stroke_width_to_length_ratio (float, optional): The maximum stroke width to length ratio. Defaults to 5.
        """
        reference_arrow = Arrow(start, end, buff=buff)
        start = reference_arrow.get_start()
        end = reference_arrow.get_end()
        reference_length = reference_arrow.get_length()

        if direction is None:
            direction = np.round((end - start) / (np.linalg.norm(end - start)), 0)
        direction = direction / np.linalg.norm(direction)

        super().__init__(
            start,
            start + direction * reference_length,
            stroke_width=stroke_width,
            buff=0,
            max_tip_length_to_length_ratio=max_tip_length_to_length_ratio,
            max_stroke_width_to_length_ratio=max_stroke_width_to_length_ratio,
            **kwargs,
        )
