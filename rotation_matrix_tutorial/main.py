from manim import *
import numpy as np

# class XHatVectorDerivation(Scene):
#     def construct(self):
#         self.show_circle()
#         self.show_circle_axis()
#         self.show_x_coodinate_axis()
#         self.show_y_hat_axis()
#         self.move_vector_and_plot_graphs()
#         # self.wait()

#     def show_circle_axis(self): 
#         circle_axis_length = 1.5

#         x_start = self.circle_origin_point + np.array([-circle_axis_length,0,0])
#         x_end = self.circle_origin_point + np.array([circle_axis_length,0,0])

#         y_start = self.circle_origin_point + np.array([0, circle_axis_length,0])
#         y_end = self.circle_origin_point + np.array([0, -circle_axis_length, 0])

#         x_axis = Line(x_start,x_end)
#         y_axis = Line(y_start,y_end)

#         self.add(x_axis, y_axis)

#     def show_circle(self):
#         self.circle_origin_point = np.array([-5,0,0])

#         circle = Circle(radius=1)
#         circle.move_to(self.circle_origin_point)
#         self.add(circle)
#         self.circle = circle

#     def show_x_coodinate_axis(self):
#         self.x_coodinate_origin_point = np.array([-1, 2, 0])

#         x_start = self.x_coodinate_origin_point + np.array([-1, 0, 0])
#         x_end = self.x_coodinate_origin_point + np.array([7, 0, 0])

#         y_start = self.x_coodinate_origin_point + np.array([0, 1.5, 0])
#         y_end = self.x_coodinate_origin_point + np.array([0, -1.5, 0])

#         x_axis = Line(x_start, x_end)
#         y_axis = Line(y_start, y_end)

#         self.add(x_axis, y_axis)
#         self.add_hat_axes_labels(self.x_coodinate_origin_point)

#     def show_y_hat_axis(self):
#         self.y_coordinate_origin_point = np.array([-1, -2, 0])

#         x_start = self.y_coordinate_origin_point + np.array([-1, 0, 0])
#         x_end = self.y_coordinate_origin_point + np.array([7, 0, 0])

#         y_start = self.y_coordinate_origin_point + np.array([0, 1.5, 0])
#         y_end = self.y_coordinate_origin_point + np.array([0, -1.5, 0])

#         x_axis = Line(x_start, x_end)
#         y_axis = Line(y_start, y_end)

#         self.add(x_axis, y_axis)
#         self.add_hat_axes_labels(self.y_coordinate_origin_point)

#     # Adds the labels for the x_hat and y_hat axes
#     def add_hat_axes_labels(self, axes_origin_point):
#         x_labels = [
#             MathTex(r"\frac{\pi}{2}"), MathTex("\pi"),
#             MathTex(r"\frac{3 \pi}{2}"), MathTex("2 \pi")
#         ]

#         y_labels = [MathTex("1"), MathTex("-1")]

#         for i in range(len(x_labels)):
#             x_labels[i].next_to(axes_origin_point + np.array([PI*(i+1)/2, 0, 0]), DOWN)
#             self.add(x_labels[i])
        
#         y_labels[0].next_to(axes_origin_point + np.array([0, 1, 0]), LEFT)
#         y_labels[1].next_to(axes_origin_point + np.array([0, -1, 0]), LEFT)
#         self.add(y_labels[0], y_labels[1])

#     def move_vector_and_plot_graphs(self):
#         self.video_length = 10.0    # seconds

#         # Starting out with dot first
#         orbit = self.circle
#         origin_point =self.circle_origin_point

#         dot = Dot(radius=0.08, color=YELLOW)
#         dot.move_to(orbit.point_from_proportion(0))
#         self.t_offset = 0
#         rate = 0.125

#         def go_around_circle(mob, dt):
#             self.t_offset += (dt * rate)
#             mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

#         def get_line_to_circle():
#             return Line(origin_point, dot.get_center(), color=BLUE)

#         self.curve_start = self.x_coodinate_origin_point

#         # Sine and Cosine curve 
#         self.radian_values = np.linspace(0, 2*np.pi, self.video_length*100)
#         self.sine_values = np.sin(self.radian_values)
#         self.cosine_values = np.cos(self.radian_values)

#         self.curve = VGroup()
#         self.curve.add(Line(self.curve_start, self.curve_start))
        
#         def get_cosine_curve():
#             last_line = self.curve[-1]
#             x = self.curve_start[0] 

#         def get_curve():
#             last_line = self.curve[-1]
#             x = self.curve_start[0] + self.t_offset*4
#             y = dot.get_center()[1]
#             new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
#             self.curve.add(new_line)

#             return self.curve

#         dot.add_updater(go_around_circle)

#         origin_to_circle_line = always_redraw(get_line_to_circle)
#         sine_curve_line = always_redraw(get_curve)

#         self.add(dot)
#         self.add(orbit, origin_to_circle_line, sine_curve_line)
#         self.wait(10.01)
#         # self.wait(5.0)

#         dot.remove_updater(go_around_circle)

class XHatVectorDerivation(Scene):
    def construct(self):
        self.e = ValueTracker(0.01)  # Tracks the end value of both functions 

        # UnitCirclePlotting
        

        # Cosine curve plotting 
        axes0 = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        axes0.add_coordinates(
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
        axes0.move_to([1, 2, 0])    # Location of axes 
        cosineCurveGraph = always_redraw(lambda : axes0.get_graph(lambda x : np.cos(x), x_range=[0, self.e.get_value()], color=GREEN))
        cosineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(cosineCurveGraph.get_end()))

        # Sine curve plotting 
        axes1 = Axes(x_range=[0, 2*PI, PI/2], x_length=3, y_range=[-1.0, 1.0, 1], y_length=2, tips=False)
        axes1.add_coordinates(
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
        axes1.move_to([1, -2, 0])    # Location of axes
        sineCurveGraph = always_redraw(lambda : axes1.get_graph(lambda x : np.sin(x), x_range=[0, self.e.get_value()], color=GREEN))
        sineCuveEndDot = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity=0.8).scale(0.5).move_to(sineCurveGraph.get_end()))
        
        # self.play(LaggedStart(
        #             Create(axes0), run_time=3, lag_ratio=(0.5)
        # ))
        self.play(Create(axes0), Create(axes1))
        self.add(cosineCurveGraph, cosineCuveEndDot, sineCurveGraph, sineCuveEndDot)
        self.play(self.e.animate.set_value(2*PI), run_time=5, rate_functions=linear)
        self.wait(1)
