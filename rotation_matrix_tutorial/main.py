from manim import *

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
