from manim import *

class RotationMatrix2D(Scene):
    def construct(self):

        rotation_matrix_2d = MobjectMatrix(
            [[MathTex(r"\cos(\theta)"), MathTex(r"-\sin(\theta)")],
            [MathTex(r"\sin(\theta)"), MathTex(r"cos(\theta)")]],
            h_buff = 2,
            bracket_h_buff = MED_SMALL_BUFF
        )

        rotation_matrix_2d_question_mark = MobjectMatrix(
            [[MathTex(r"???"), MathTex(r"???")],
            [MathTex(r"???"), MathTex(r"???")]],
            h_buff = 2,
        )

        # rotation_matrix_2d_how = MobjectMatrix(
        #     [[MathTex(r"H"), MathTex(r"W")],
        #     [MathTex(r"O"), MathTex(r"?")]],
        #     h_buff = 2,
        # )

        # rotation_matrix_2d_why = MobjectMatrix(
        #     [[MathTex(r"W"), MathTex(r"H")],
        #     [MathTex(r"Y"), MathTex(r"?")]],
        #     h_buff = 2,
        # )

        self.play(Create(rotation_matrix_2d), run_time=2, lag_ratio=0.1)
        self.wait(1)
        self.play(Transform(rotation_matrix_2d, rotation_matrix_2d_question_mark), run_time=1)
        self.wait(2)
        # self.play(ReplacementTransform(Transform(rotation_matrix_2d, rotation_matrix_2d_question_mark), rotation_matrix_2d_how), run_time=2)
        # self.wait(1)
        # self.play(Transform(rotation_matrix_2d_how, rotation_matrix_2d_why), run_time=2)
        # self.wait(1)

class VectorConceptions(Scene):
    def construct(self):
        pet_vector_example = MobjectMatrix(
            [MathTex("cats"),
            MathTex("dogs")],
        )

        vector_component_example =  MobjectMatrix(
            [MathTex("x"),
            MathTex("y"),
            MathTex("z")],
        )

        self.play(Create(pet_vector_example), run_time=2, lag_ratio=0.1)
        self.wait(3)
        self.play(Transform(pet_vector_example, vector_component_example), run_time=1)
        self.wait(2)

class XHatVectorDerivation(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # --------------- Unit circle plotting ---------------
        unit_circle_axes = PolarPlane(size=3,
                                    azimuth_units="PI radians",
                                    background_line_style={"stroke_color": BLACK,
                                                            "stroke_width" : 2,
                                                            "stroke_opacity" : 1
                                                            }
        )
        unit_circle_axes.move_to([-4, 0, 0])

        unit_circle_graph = always_redraw(lambda : 
                                            ParametricFunction(lambda t : unit_circle_axes.polar_to_point(3, t),
                                                                t_range=[0, self.e.get_value()],
                                                                color = GREEN
                                            )
        )
        unit_circle_x_vector = always_redraw(lambda : Line(start=unit_circle_axes.get_origin(), end=unit_circle_graph.get_end(), color=RED).add_tip())

        # --------------- X-component curve plotting ---------------
        x_component_plot_axes = Axes(x_range=[0, 2*PI, PI/2], 
                                x_length=3, 
                                y_range=[-1.0, 1.0, 1], 
                                y_length=2, 
                                tips=False
        )
        x_component_plot_axes.add_coordinates(
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
        x_component_plot_axes.move_to([1, 2, 0])    # Location of axes 
        x_component_plot_graph = always_redraw(lambda : x_component_plot_axes.plot(lambda x : np.cos(x), 
                                                                            [0, self.e.get_value()], 
                                                                            color=GREEN)
        )
        x_component_end_dot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(x_component_plot_graph.get_end()))

        # --------------- Y-component curve plotting ---------------
        y_component_plot_axes = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        y_component_plot_axes.add_coordinates(
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
        y_component_plot_axes.move_to([1, -2, 0])    # Location of axes
        y_component_plot_graph = always_redraw(lambda : y_component_plot_axes.plot(lambda x : np.sin(x), 
                                                                        [0, self.e.get_value()], 
                                                                        color=GREEN)
        )
        y_component_end_dot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(y_component_plot_graph.get_end()))
        
        # Playing out the animation 
        self.play(Create(unit_circle_axes), Create(x_component_plot_axes), Create(y_component_plot_axes), run_time=3, lag_ratio=0.25)
        self.add(x_component_plot_graph, x_component_end_dot, y_component_plot_graph, y_component_end_dot, unit_circle_graph, unit_circle_x_vector)
        self.wait(1)
        self.play(self.e.animate.set_value(2*PI), run_time=6, rate_functions=linear)
        self.wait(1)

class YHatVectorDerivation(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # --------------- Unit circle plotting ---------------
        unit_circle_axes = PolarPlane(size=3,
                                    azimuth_units="PI radians",
                                    background_line_style={"stroke_color": BLACK,
                                                            "stroke_width" : 2,
                                                            "stroke_opacity" : 1
                                                            }
        )
        unit_circle_axes.move_to([-4, 0, 0])

        unit_circle_graph = always_redraw(lambda : 
                                            ParametricFunction(lambda t : unit_circle_axes.polar_to_point(3, t + PI/2),
                                                                t_range=[0, self.e.get_value()],
                                                                color = GREEN
                                            )
        )
        unit_circle_y_vector = always_redraw(lambda : Line(start=unit_circle_axes.get_origin(), end=unit_circle_graph.get_end(), color=BLUE).add_tip())

        # --------------- X-component curve plotting ---------------
        x_component_plot_axes = Axes(x_range=[0, 2*PI, PI/2], 
                                x_length=3, 
                                y_range=[-1.0, 1.0, 1], 
                                y_length=2, 
                                tips=False
        )
        x_component_plot_axes.add_coordinates(
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
        x_component_plot_axes.move_to([1, 2, 0])    # Location of axes 
        x_component_plot_graph = always_redraw(lambda : x_component_plot_axes.plot(lambda x : -np.sin(x), 
                                                                            [0, self.e.get_value()], 
                                                                            color=GREEN)
        )
        x_component_end_dot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(x_component_plot_graph.get_end()))

        # --------------- Y-component curve plotting ---------------
        y_component_plot_axes = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        y_component_plot_axes.add_coordinates(
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
        y_component_plot_axes.move_to([1, -2, 0])    # Location of axes
        y_component_plot_graph = always_redraw(lambda : y_component_plot_axes.plot(lambda x : np.cos(x), 
                                                                        [0, self.e.get_value()], 
                                                                        color=GREEN)
        )
        y_component_end_dot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(y_component_plot_graph.get_end()))
        
        # Playing out the animation 
        self.play(Create(unit_circle_axes), Create(x_component_plot_axes), Create(y_component_plot_axes), run_time=3, lag_ratio=0.25)
        self.add(x_component_plot_graph, x_component_end_dot, y_component_plot_graph, y_component_end_dot, unit_circle_graph, unit_circle_y_vector)
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
