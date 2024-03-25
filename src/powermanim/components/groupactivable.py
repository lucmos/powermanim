import abc
import typing as T
from collections import defaultdict

from manim import *


class ActivableMobject(Group):
    def __init__(
        self,
        inactive_vmobject: Mobject,
        active_vmobject: Mobject,
        start_active: bool = False,
        activation_anim_run_time: float = 1.0,
        deactivation_anim_run_time: float = 1.0,
        group: T.Optional[int] = None,
    ) -> None:
        self.is_active = start_active
        self.activation_anim_run_time = activation_anim_run_time
        self.deactivation_anim_run_time = deactivation_anim_run_time
        self.group = group
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
        self.group = group

    @property
    def obj(self) -> Mobject:
        return self[0]

    @abc.abstractmethod
    def _get_activation_anim(self):
        raise NotImplementedError

    def activate(self) -> Animation:
        if self.is_active:
            raise ValueError("The object is already active.")
        self.is_active = True
        return self._get_activation_anim()

    @abc.abstractmethod
    def _get_deactivation_anim(self):
        raise NotImplementedError

    def deactivate(self) -> Animation:
        if not self.is_active:
            raise ValueError("The object is already inactive.")
        self.is_active = False
        return self._get_deactivation_anim()


class VActivable(ActivableMobject):
    def __init__(
        self,
        inactive_vmobject: VMobject,
        active_vmobject: VMobject,
        start_active: bool = False,
        activation_anim_run_time: float = 1.0,
        deactivation_anim_run_time: float = 1.0,
        group: T.Optional[int] = None,
    ) -> None:
        self.active_stroke_opacities = [x.stroke_opacity for x in active_vmobject.get_family()]
        self.active_fill_opacities = [x.fill_opacity for x in active_vmobject.get_family()]
        self.inactive_stroke_opacities = [x.stroke_opacity for x in inactive_vmobject.get_family()]
        self.inactive_fill_opacities = [x.fill_opacity for x in inactive_vmobject.get_family()]

        super().__init__(
            inactive_vmobject=inactive_vmobject,
            active_vmobject=active_vmobject,
            start_active=start_active,
            activation_anim_run_time=activation_anim_run_time,
            deactivation_anim_run_time=deactivation_anim_run_time,
            group=group,
        )

    def _get_activation_anim(self) -> Animation:
        target = self.active_vmobject.copy()
        for subobj, stroke_opacity, fill_opacity in zip(
            target.get_family(), self.active_stroke_opacities, self.active_fill_opacities
        ):
            subobj.set_fill(opacity=fill_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False, background=True)
        return Transform(self.obj, target, run_time=self.activation_anim_run_time)

    def _get_deactivation_anim(self) -> Animation:
        target = self.inactive_vmobject.copy()
        for subobj, stroke_opacity, fill_opacity in zip(
            target.get_family(), self.inactive_stroke_opacities, self.inactive_fill_opacities
        ):
            subobj.set_fill(opacity=fill_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False)
            subobj.set_stroke(opacity=stroke_opacity, family=False, background=True)

        return Transform(self.obj, target, run_time=self.deactivation_anim_run_time)


class VAutoActivable(VActivable):
    def __init__(
        self,
        vmobject: VMobject,
        active_fill_opacity: T.Optional[float] = 1.0,
        active_stroke_opacity: T.Optional[float] = 1.0,
        inactive_fill_opacity: T.Optional[float] = 0.35,
        inactive_stroke_opacity: T.Optional[float] = 0.35,
        scale_active: T.Optional[float] = 1.1,
        scale_about_point=None,
        scale_about_edge=LEFT,
        activation_anim_run_time: float = 1,
        deactivation_anim_run_time: float = 1,
        group: T.Optional[int] = None,
    ) -> None:
        """Activable component that automatically creates the active and inactive VMobjects.

        Args:
            vmobject (VMobject): The object to activate or deactivate VMobject.
            active_fill_opacity (float): The fill opacity of the active VMobject.
            active_stroke_opacity (float): The stroke opacity of the active VMobject.
            inactive_fill_opacity (float): The fill opacity of the inactive VMobject.
            inactive_stroke_opacity (float): The stroke opacity of the inactive VMobject.
            scale_active (float): The scale of the active VMobject.
            scale_about_point (np.ndarray): The point to scale about.
            scale_about_edge (np.ndarray): The edge to scale about.
            group (int): The group to which the object belongs.
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
        super().__init__(
            inactive_vmobject=inactive_obj,
            active_vmobject=active_obj,
            start_active=False,
            group=group,
            activation_anim_run_time=activation_anim_run_time,
            deactivation_anim_run_time=deactivation_anim_run_time,
        )


class ImageAutoActivable(ActivableMobject):
    def __init__(
        self,
        vmobject: Mobject,
        active_opacity: T.Optional[float] = 1.0,
        inactive_opacity: T.Optional[float] = 0.35,
        scale_active: T.Optional[float] = 1.1,
        scale_about_point=None,
        scale_about_edge=ORIGIN,
        activation_anim_run_time: float = 1.0,
        deactivation_anim_run_time: float = 1.0,
        group: T.Optional[int] = None,
    ) -> None:
        """Activable component that automatically creates the active and inactive Mobjects.

        Args:
            vmobject (Mobject): The object to activate or deactivate Mobject.
            active_opacity (float): The fill opacity of the active Mobject.
            inactive_opacity (float): The fill opacity of the inactive Mobject.
            scale_active (float): The scale of the active Mobject.
            scale_about_point (np.ndarray): The point to scale about.
            scale_about_edge (np.ndarray): The edge to scale about.
            group (int): The group to which the object belongs.
        """
        self.active_opacity = active_opacity
        self.inactive_opacity = inactive_opacity
        self.scale_active = scale_active
        self.scale_about_point = scale_about_point
        self.scale_about_edge = scale_about_edge

        active_obj = vmobject.copy()
        if self.scale_active is not None:
            active_obj.scale(self.scale_active, about_point=self.scale_about_point, about_edge=self.scale_about_edge)
        if self.active_opacity is not None:
            active_obj.set_opacity(self.active_opacity)

        inactive_obj = vmobject.copy()
        if self.inactive_opacity is not None:
            inactive_obj.set_opacity(self.inactive_opacity)

        super().__init__(
            inactive_vmobject=inactive_obj,
            active_vmobject=active_obj,
            start_active=False,
            activation_anim_run_time=activation_anim_run_time,
            deactivation_anim_run_time=deactivation_anim_run_time,
            group=group,
        )

    def _get_activation_anim(self) -> Animation:
        return self.obj.animate.set_opacity(self.active_opacity)

    def _get_deactivation_anim(self) -> Animation:
        return self.obj.animate.set_opacity(self.inactive_opacity)


class GroupActivable(Group):
    def __init__(
        self,
        *args: Mobject,
        anim_lag_ratio: float = 0,
        **kwargs: Mobject,
    ) -> None:
        """Group component that can activate a subset of its submobjects.

        Args:
            *args: Submobjects to be added to the VGroup.
            anim_lag_ratio (float): The lag ratio of the animation.
            **kwargs: Keyword arguments to be passed to the VGroup.
        """
        args_activable = (
            (
                (VAutoActivable(x) if isinstance(x, VMobject) else ImageAutoActivable(x))
                if not isinstance(x, ActivableMobject)
                else x
            )
            for x in args
        )
        super().__init__(*args_activable, **kwargs)

        self.anim_lag_ratio = anim_lag_ratio

        self.previously_active_idxs = []
        self.actived = 0

        # Resolve groups
        groups = [item.group for item in self.submobjects]

        # If there is a None and aso something else
        if (None in groups) and len(set(groups)) != 1:
            raise ValueError("The groups must be specified for all or no bullets at all.")

        self.group2items: Dict[int, T.Set[VActivable]] = defaultdict(set)
        for i, obj in enumerate(self.submobjects):
            group = obj.group
            if group is None:
                group = i
            self.group2items[group].add(obj)

    @property
    def ngroups(self) -> int:
        return len(self.group2items)

    def activate(self, indices: T.Union[int, T.Sequence[int]]) -> AnimationGroup:
        """Activates the submobjects in the given indices in the scene.

        Args:
            scene:
                The scene in which the animation is played.

            indices:
                The indices to activate. If a single integer is given, only that index is activated.
                If a sequence of integers is given, all indices in the sequence are activated. The
                previously activated indices are deactivated smoothly.
        """
        anims = []

        if not isinstance(indices, T.Sequence):
            indices = [indices]

        for to_activate in indices:
            if to_activate in self.previously_active_idxs:
                continue
            anims.append(AnimationGroup(*(x.activate() for x in self.group2items[to_activate])))

        if self.previously_active_idxs:
            for previously_active_idx in self.previously_active_idxs:
                if previously_active_idx not in indices:
                    anims.append(AnimationGroup(*(x.deactivate() for x in self.group2items[previously_active_idx])))

        self.previously_active_idxs = indices

        return AnimationGroup(*anims, lag_ratio=self.anim_lag_ratio)

    def also_next(self) -> Animation:
        """Highlights also the next item in the VGroup."""
        self.actived += 1

        if self.actived > len(self):
            raise StopIteration("No more elements to activate.")

        return self.activate(indices=list(range(self.actived)))

    def only_next(self) -> Animation:
        """Highlights only the next item in the VGroup."""
        if self.actived > len(self):
            raise StopIteration("No more elements to activate.")
        anims = self.activate(indices=self.actived)
        self.actived += 1
        return anims

    def clear(self) -> Animation:
        """Clears the VGroup hightlighting."""
        anims = self.activate(indices=[])
        self.actived = 0
        return anims

    def all(self) -> Animation:
        """Highlights all the VGroup."""
        return self.activate(indices=list(range(len(self))))
