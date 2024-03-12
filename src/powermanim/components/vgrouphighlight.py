import typing as T

from manim import *


class Highlightable(VGroup):
    def __init__(
        self,
        inactive_vmobject: VMobject,
        active_vmobject: VMobject,
        start_active: bool = False,
        activation_anim_run_time: float = 1.0,
        deactivation_anim_run_time: float = 1.0,
    ) -> None:
        self.active_stroke_opacities = [x.stroke_opacity for x in active_vmobject.get_family()]
        self.active_fill_opacities = [x.fill_opacity for x in active_vmobject.get_family()]
        self.inactive_stroke_opacities = [x.stroke_opacity for x in inactive_vmobject.get_family()]
        self.inactive_fill_opacities = [x.fill_opacity for x in inactive_vmobject.get_family()]

        super().__init__(
            active_vmobject.copy() if start_active else inactive_vmobject.copy(),
            active_vmobject.set_opacity(0),
            inactive_vmobject.set_opacity(0),
        )

        self.active_vmobject = active_vmobject
        self.inactive_vmobject = inactive_vmobject

        self.is_active = start_active
        self.activation_anim_run_time = activation_anim_run_time
        self.deactivation_anim_run_time = deactivation_anim_run_time

    @property
    def obj(self) -> VMobject:
        return self[0]

    def get_activation_anim(self) -> Animation:
        if self.is_active:
            raise ValueError("The object is already active.")
        self.is_active = True

        target = self.active_vmobject.copy()
        for subobj, stroke_opacity, fill_opacity in zip(
            target.get_family(), self.active_stroke_opacities, self.active_fill_opacities
        ):
            subobj.set_fill(opacity=fill_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False, background=True)
        return Transform(self.obj, target, run_time=self.activation_anim_run_time)

    def get_deactivation_anim(self) -> Animation:
        if not self.is_active:
            raise ValueError("The object is already inactive.")
        self.is_active = False

        target = self.inactive_vmobject.copy()
        for subobj, stroke_opacity, fill_opacity in zip(
            target.get_family(), self.inactive_stroke_opacities, self.inactive_fill_opacities
        ):
            subobj.set_fill(opacity=fill_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False, background=True)

        return Transform(self.obj, target, run_time=self.deactivation_anim_run_time)


class AutoHighlightable(Highlightable):
    def __init__(
        self,
        vmobject: VMobject,
        active_fill_opacity: T.Optional[float] = 1.0,
        active_stroke_opacity: T.Optional[float] = 1.0,
        inactive_fill_opacity: T.Optional[float] = 0.5,
        inactive_stroke_opacity: T.Optional[float] = 0.5,
        scale_active: T.Optional[float] = 1.0,
        scale_about_point=None,
        scale_about_edge=LEFT,
    ) -> None:
        """Highlightable component that automatically creates the active and inactive VMobjects.

        Args:
            vmobject (VMobject): The object to activate or deactivate VMobject.
            active_fill_opacity (float): The fill opacity of the active VMobject.
            active_stroke_opacity (float): The stroke opacity of the active VMobject.
            inactive_fill_opacity (float): The fill opacity of the inactive VMobject.
            inactive_stroke_opacity (float): The stroke opacity of the inactive VMobject.
            scale_active (float): The scale of the active VMobject.
            scale_about_point (np.ndarray): The point to scale about.
            scale_about_edge (np.ndarray): The edge to scale about.
        """
        self.active_fill_opacity = active_fill_opacity
        self.active_stroke_opacity = active_stroke_opacity
        self.inactive_fill_opacity = inactive_fill_opacity
        self.inactive_stroke_opacity = inactive_stroke_opacity
        self.scale_active = scale_active
        self.scale_about_point = scale_about_point
        self.scale_about_edge = scale_about_edge

        active_obj = vmobject.copy()
        if self.scale_active is not None:
            active_obj.scale(self.scale_active, about_point=self.scale_about_point, about_edge=self.scale_about_edge)
        if self.active_fill_opacity is not None:
            active_obj.set_fill(opacity=self.active_fill_opacity)
        if self.active_stroke_opacity is not None:
            active_obj.set_stroke(opacity=self.active_stroke_opacity)

        inactive_obj = vmobject.copy()
        if self.inactive_fill_opacity is not None:
            inactive_obj.set_fill(opacity=self.inactive_fill_opacity)
        if self.inactive_stroke_opacity is not None:
            inactive_obj.set_stroke(opacity=self.inactive_stroke_opacity)
        super().__init__(inactive_vmobject=inactive_obj, active_vmobject=active_obj, start_active=False)


class VGroupHighlight(VGroup):
    def __init__(
        self,
        *args: VMobject,
        anim_lag_ratio: float = 0,
        **kwargs: VMobject,
    ) -> None:
        """Group component that can highlight a subset of its submobjects.

        Args:
            *args: Submobjects to be added to the VGroup.
            anim_lag_ratio (float): The lag ratio of the animation.
            **kwargs: Keyword arguments to be passed to the VGroup.
        """
        args_highlightable = (AutoHighlightable(x) if not isinstance(x, Highlightable) else x for x in args)
        super().__init__(*args_highlightable, **kwargs)

        self.anim_lag_ratio = anim_lag_ratio

        self.previously_active_idxs = []
        self.highlighted = 0

    def highlight(self, indices: T.Union[int, T.Sequence[int]]) -> AnimationGroup:
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
            if to_highlight in self.previously_active_idxs:
                continue
            anims.append(self.submobjects[to_highlight].get_activation_anim())

        if self.previously_active_idxs:
            for previously_active_idx in self.previously_active_idxs:
                if previously_active_idx not in indices:
                    anims.append(self.submobjects[previously_active_idx].get_deactivation_anim())

        self.previously_active_idxs = indices

        return AnimationGroup(*anims, lag_ratio=self.anim_lag_ratio)

    def also_next(self) -> Animation:
        """Highlights also the next item in the VGroup."""
        self.highlighted += 1

        if self.highlighted > len(self):
            raise StopIteration("No more elements to highlight.")

        return self.highlight(indices=list(range(self.highlighted)))

    def only_next(self) -> Animation:
        """Highlights only the next item in the VGroup."""
        if self.highlighted > len(self):
            raise StopIteration("No more elements to highlight.")
        anims = self.highlight(indices=self.highlighted)
        self.highlighted += 1
        return anims

    def clear(self) -> Animation:
        """Clears the VGroup hightlighting."""
        anims = self.highlight(indices=[])
        self.highlighted = 0
        return anims

    def all(self) -> Animation:
        """Highlights all the VGroup."""
        return self.highlight(indices=list(range(len(self))))
