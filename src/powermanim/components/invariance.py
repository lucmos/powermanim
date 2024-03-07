from typing import Tuple

from manim import *
from scipy.stats import ortho_group


class Invariance(VGroup):
    COLORS = [
        ORANGE,
        BLUE,
        TEAL,
        GREEN,
        YELLOW,
        GOLD,
        RED,
        MAROON,
        PURPLE,
        PINK,
    ]

    def __init__(self, axis):
        np.random.seed(seed=1)
        self.active_opacity = 0.8
        self.inactive_opacity = 0.25

        self.axis = axis
        self.points_coords_orig = np.random.rand(17, 3) * 2 - 1
        self.points_coords_orig[:, -1] = 0
        self.points_coords = self.axis.coords_to_point(self.points_coords_orig)

        self.dots = [
            Dot(
                self.points_coords[i],
                fill_opacity=self.active_opacity,
                color=self.COLORS[i % len(self.COLORS)],
                z_index=1,
            )
            for i in range(len(self.points_coords))
        ]

        super().__init__(self.axis, *self.dots)

    def transformation_anim(self, transformation: np.ndarray, bias: np.ndarray = 0, run_time: float = 1.0):
        self.points_coords = self.axis.coords_to_point(np.matmul(self.points_coords_orig, transformation) + bias)

        return AnimationGroup(
            *(self.dots[i].animate.move_to(self.points_coords[i]) for i in range(len(self.points_coords))),
            run_time=run_time,
        )

    def get_random_ortho_matrix(self):
        random_ortho = np.zeros((3, 3))
        random_ortho[:2, :2] = ortho_group.rvs(2)
        return random_ortho

    def radii_anim(self, point_indices, line_overshoot: float = 1.25, run_time=1.0) -> Tuple[Animation, List[Line]]:
        lines = []
        for point_index in point_indices:
            point = self.axis.p2c(self.points_coords[point_index])
            point = point / np.linalg.norm(point)

            line = DashedLine(self.axis.coords_to_point(*ORIGIN), self.axis.c2p(*(point * line_overshoot))).set_opacity(
                0.5
            )
            lines.append(line)

        return AnimationGroup(*[Create(line) for line in lines], run_time=run_time), lines

    def rescale_along_radius_anim(
        self, point_indices, n_iters=3, max_radius=0.95, min_radius=0.2, lines=[]
    ) -> AnimationGroup:
        orig_points = [self.axis.p2c(self.points_coords[point_index]) for point_index in point_indices]

        hide_others = AnimationGroup(
            *[
                self.dots[point_index].animate.set_opacity(self.inactive_opacity)
                for point_index in range(len(self.dots))
                if point_index not in point_indices
            ],
        )

        move_some = []
        for point_idx, point in zip(point_indices, orig_points):
            point_traj = np.tile(point[None], (2 * n_iters + 2, 1))
            point_traj[1:-1, :] /= np.linalg.norm(point_traj, axis=-1, keepdims=True)[1:-1]
            point_traj[1:-1, :] *= np.tile(np.asarray([max_radius, min_radius]), n_iters)[..., None]

            path = VMobject()
            path.set_points_smoothly(self.axis.coords_to_point(point_traj))
            move_some.append(MoveAlongPath(self.dots[point_idx], path, run_time=1.75))

        show_others = AnimationGroup(VGroup(*self.dots).animate.set_opacity(self.active_opacity))

        animations = [
            AnimationGroup(hide_others, run_time=1),
            AnimationGroup(*move_some, lag_ratio=0.05, run_time=n_iters),
        ]

        if lines:
            animations.append(
                AnimationGroup(
                    *(Uncreate(x) for x in lines),
                    show_others,
                    lag_ratio=0.5,
                    run_time=1,
                ),
            )
        else:
            animations.append(AnimationGroup(show_others, run_time=1))
        return Succession(*animations)

    def rescale_all_to_unit_anim(self, run_time=2.0) -> AnimationGroup:
        return AnimationGroup(
            *(
                self.dots[i].animate.move_to(
                    self.axis.c2p(
                        *(self.axis.p2c(self.points_coords[i]) / np.linalg.norm(self.axis.p2c(self.points_coords[i])))
                    )
                )
                for i in range(len(self.points_coords))
            ),
            run_time=run_time,
        )
