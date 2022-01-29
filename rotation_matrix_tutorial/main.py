from manim import *
from numpy import cos

class RotationMatrix2D(Scene):
    def construct(self):

        rotationMatrix2D = MobjectMatrix([
            [MathTex(r"\cos()")],
            [MathTex(r"\sin()")]
        ])

        self.add(rotationMatrix2D)


class XHatVectorDerivation(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # --------------- Unit circle plotting ---------------
        unitCircleAxes = PolarPlane(size=3,
                                    azimuth_units="PI radians",
                                    background_line_style={"stroke_color": BLACK,
                                                            "stroke_width" : 2,
                                                            "stroke_opacity" : 1
                                                            }
        )
        unitCircleAxes.move_to([-4, 0, 0])

        unitCircleGraph = always_redraw(lambda : 
                                            ParametricFunction(lambda t : unitCircleAxes.polar_to_point(3, t),
                                                                t_range=[0, self.e.get_value()],
                                                                color = GREEN
                                            )
        )
        unitCircleXVector = always_redraw(lambda : Line(start=unitCircleAxes.get_origin(), end=unitCircleGraph.get_end(), color=RED).add_tip())

        # --------------- Cosine curve plotting ---------------
        cosineCurveAxes = Axes(x_range=[0, 2*PI, PI/2], 
                                x_length=3, 
                                y_range=[-1.0, 1.0, 1], 
                                y_length=2, 
                                tips=False
        )
        cosineCurveAxes.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        cosineCurveAxes.move_to([1, 2, 0])    # Location of axes 
        cosineCurveGraph = always_redraw(lambda : cosineCurveAxes.get_graph(lambda x : np.cos(x), 
                                                                            x_range=[0, self.e.get_value()], 
                                                                            color=GREEN)
        )
        cosineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(cosineCurveGraph.get_end()))

        # --------------- Sine curve plotting ---------------
        sineCurveAxes = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        sineCurveAxes.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        sineCurveAxes.move_to([1, -2, 0])    # Location of axes
        sineCurveGraph = always_redraw(lambda : sineCurveAxes.get_graph(lambda x : np.sin(x), 
                                                                        x_range=[0, self.e.get_value()], 
                                                                        color=GREEN)
        )
        sineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(sineCurveGraph.get_end()))
        
        # Playing out the animation 
        self.play(Create(unitCircleAxes), Create(cosineCurveAxes), Create(sineCurveAxes), run_time=3, lag_ratio=0.25)
        self.add(cosineCurveGraph, cosineCuveEndDot, sineCurveGraph, sineCuveEndDot, unitCircleGraph, unitCircleXVector)
        self.wait(1)
        self.play(self.e.animate.set_value(2*PI), run_time=6, rate_functions=linear)
        self.wait(1)


class YHatVectorDerivation(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # --------------- Unit circle plotting ---------------
        unitCircleAxes = PolarPlane(size=3,
                                    azimuth_units="PI radians",
                                    background_line_style={"stroke_color": BLACK,
                                                            "stroke_width" : 2,
                                                            "stroke_opacity" : 1
                                                            }
        )
        unitCircleAxes.move_to([-4, 0, 0])

        unitCircleGraph = always_redraw(lambda : 
                                            ParametricFunction(lambda t : unitCircleAxes.polar_to_point(3, t + PI/2),
                                                                t_range=[0, self.e.get_value()],
                                                                color = GREEN
                                            )
        )
        unitCircleXVector = always_redraw(lambda : Line(start=unitCircleAxes.get_origin(), end=unitCircleGraph.get_end(), color=BLUE_A).add_tip())

        # --------------- Cosine curve plotting ---------------
        cosineCurveAxes = Axes(x_range=[0, 2*PI, PI/2], 
                                x_length=3, 
                                y_range=[-1.0, 1.0, 1], 
                                y_length=2, 
                                tips=False
        )
        cosineCurveAxes.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        cosineCurveAxes.move_to([1, 2, 0])    # Location of axes 
        cosineCurveGraph = always_redraw(lambda : cosineCurveAxes.get_graph(lambda x : np.cos(x), 
                                                                            x_range=[0, self.e.get_value()], 
                                                                            color=GREEN)
        )
        cosineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(cosineCurveGraph.get_end()))

        # --------------- Sine curve plotting ---------------
        sineCurveAxes = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        sineCurveAxes.add_coordinates(
            {
                PI/2 : MathTex(r"\frac{\pi}{2}"),
                PI : MathTex("\pi"),
                3*PI/2 : MathTex(r"\frac{3 \pi}{2}"),
                2*PI : MathTex("2 \pi")
            },
            {
                -1.0 : MathTex("-1"),
                0.0 : MathTex("0"),
                1.0 : MathTex("1"),
            }
        )
        sineCurveAxes.move_to([1, -2, 0])    # Location of axes
        sineCurveGraph = always_redraw(lambda : sineCurveAxes.get_graph(lambda x : np.sin(x), 
                                                                        x_range=[0, self.e.get_value()], 
                                                                        color=GREEN)
        )
        sineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(sineCurveGraph.get_end()))
        
        # Playing out the animation 
        self.play(Create(unitCircleAxes), Create(cosineCurveAxes), Create(sineCurveAxes), run_time=3, lag_ratio=0.25)
        self.add(cosineCurveGraph, cosineCuveEndDot, sineCurveGraph, sineCuveEndDot, unitCircleGraph, unitCircleXVector)
        self.wait(1)
        self.play(self.e.animate.set_value(2*PI), run_time=6, rate_functions=linear)
        self.wait(1)


class DrawingUnitCircle(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # Unit circle plotting
        unitCircleAxes = PolarPlane(size=3.5,
                                    azimuth_units=None,
                                    background_line_style={"stroke_color": BLACK,
                                                            "stroke_width" : 2,
                                                            "stroke_opacity" : 1
                                                            }
        )
        unitCircleAxes.move_to([-4, 0, 0])

        unitCircleGraph = always_redraw(lambda : 
                                            ParametricFunction(lambda t : unitCircleAxes.polar_to_point(3, t),
                                                                t_range=[0, self.e.get_value()],
                                                                color = GREEN
                                            )
        )
        unitCircleDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(unitCircleGraph.get_end()))
        unitCircleXVector = always_redraw(lambda : Line(start=unitCircleAxes.get_origin(), end=unitCircleGraph.get_end(), color=RED).add_tip())

        # Playing out the animation 
        self.play(Create(unitCircleAxes), run_time=1.5, lag_ratio=0.25)
        self.add(unitCircleGraph, unitCircleXVector)
        self.play(self.e.animate.set_value(2*PI), run_time=5, rate_functions=linear)
        self.wait(1)

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
