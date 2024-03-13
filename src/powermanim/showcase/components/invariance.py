from manim import *

from powermanim import Invariance
from powermanim.showcase.showcasescene import ShowcaseScene


class InvarianceShowcase(ShowcaseScene):
    def showcasing():
        return Invariance

    def construct(self):
        invshowcase: Invariance = Invariance(
            Axes(
                x_range=[-1.5, 1.5],
                y_range=[-1.5, 1.5],
                x_length=4,
                y_length=4,
                axis_config={"include_ticks": False},
            ).scale(1.5)
        )

        self.add(invshowcase)

        for i in [
            np.pi * 0.1,
            np.pi * 0.15,
            np.pi * 0.2,
        ]:
            self.play(
                invshowcase.transformation_anim(
                    np.array(
                        [
                            [np.cos(i), -np.sin(i), 0],
                            [np.sin(i), np.cos(i), 0],
                            [0, 0, 1],
                        ]
                    ),
                    run_time=0.5,
                )
            )

        for i in range(2, 5):
            self.play(
                invshowcase.transformation_anim(
                    invshowcase.get_random_ortho_matrix(),
                    run_time=0.5,
                )
            )

        point_indices = [0, 1, 2, 7, 8]
        radii_anim, lines = invshowcase.radii_anim(point_indices, run_time=0.275)
        self.play(radii_anim)

        self.play(invshowcase.rescale_along_radius_anim(point_indices, lines=lines))

        self.play(
            invshowcase.rescale_all_to_unit_anim(
                run_time=1.0,
            )
        )
