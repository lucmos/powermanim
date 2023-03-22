import typing as T

from manim import *


class VGroupHighlight(VGroup):
    def __init__(
        self,
        *args: VMobject,
        anim_run_time: float = 1.0,
        anim_lag_ratio: float = 0,
        active_opacity: float = 1.0,
        scale_active: float = 1.0,
        scale_about_point=None,
        scale_about_edge=None,
        **kwargs: VMobject,
    ) -> None:
        """Group component that can highlight a subset of its submobjects.

        Args:
            *args: Submobjects to be added to the VGroup.
            anim_run_time (float): The run time of the animation.
            anim_lag_ratio (float): The lag ratio of the animation.
            active_opacity (float): The opacity of the highlighted submobjects.
            scale_active (float): The scale of the highlighted submobjects.
            scale_about_point (np.ndarray): The point to scale about.
            scale_about_edge (np.ndarray): The edge to scale about.
            **kwargs: Keyword arguments to be passed to the VGroup.
        """
        super().__init__(*args, **kwargs)

        for x in self.submobjects:
            x.save_state()

        self.anim_run_time = anim_run_time
        self.anim_lag_ratio = anim_lag_ratio
        self.active_opacity = active_opacity
        self.scale_active = scale_active
        self.scale_about_point = scale_about_point
        self.scale_about_edge = scale_about_edge

        self.previously_active_idxs = []

    def highlight(self, scene: Scene, indices: T.Union[int, T.Sequence[int]]) -> None:
        """Highlights the submobjects in the given indices in the scene.

        Args:
            scene:
                The scene in which the animation is played.

            indices:
                The indices to highlight. If a single integer is given, only that index is highlighted.
                If a sequence of integers is given, all indices in the sequence are highlighted. The
                previously highlighted indices are dehighlighted smoothly.
        """
        anims = []

        if not isinstance(indices, T.Sequence):
            indices = [indices]

        for to_highlight in indices:
            self.submobjects[to_highlight].target = self.submobjects[to_highlight].saved_state.copy()
            self.submobjects[to_highlight].target.scale(
                self.scale_active,
                about_point=self.scale_about_point,
                about_edge=self.scale_about_edge,
            )
            self.submobjects[to_highlight].target.set_opacity(self.active_opacity)
            anims.append(MoveToTarget(self.submobjects[to_highlight]))

        if self.previously_active_idxs:
            for previously_active_idx in self.previously_active_idxs:
                if previously_active_idx not in indices:
                    anims.append(
                        self.submobjects[previously_active_idx].animate.restore(),
                    )

        self.previously_active_idxs = indices

        scene.play(
            AnimationGroup(*anims, lag_ratio=self.anim_lag_ratio),
            run_time=self.anim_run_time,
        )
