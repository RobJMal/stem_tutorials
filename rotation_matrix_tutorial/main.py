from manim import *

class XHatVectorDerivation(Scene):
    def construct(self):
        self.show_circle()
        self.show_circle_axis()
        self.show_x_hat_axis()
        self.show_y_hat_axis()

    def show_circle_axis(self): 
        circle_axis_length = 1.5

        x_start = self.circle_origin_point + np.array([-circle_axis_length,0,0])
        x_end = self.circle_origin_point + np.array([circle_axis_length,0,0])

        y_start = self.circle_origin_point + np.array([0, circle_axis_length,0])
        y_end = self.circle_origin_point + np.array([0, -circle_axis_length, 0])

        x_axis = Line(x_start,x_end)
        y_axis = Line(y_start,y_end)

        self.add(x_axis, y_axis)

    def show_circle(self):
        self.circle_origin_point = np.array([-5,0,0])

        circle = Circle(radius=1)
        circle.move_to(self.circle_origin_point)
        self.add(circle)
        self.circle = circle

    def show_x_hat_axis(self):
        self.x_hat_origin_point = np.array([0, 2, 0])

        x_start = self.x_hat_origin_point + np.array([-1, 0, 0])
        x_end = self.x_hat_origin_point + np.array([6, 0, 0])

        y_start = self.x_hat_origin_point + np.array([0, 1.5, 0])
        y_end = self.x_hat_origin_point + np.array([0, -1.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)

    def show_y_hat_axis(self):
        self.y_hat_origin_point = np.array([0, -2, 0])

        x_start = self.y_hat_origin_point + np.array([-1, 0, 0])
        x_end = self.y_hat_origin_point + np.array([6, 0, 0])

        y_start = self.y_hat_origin_point + np.array([0, 1.5, 0])
        y_end = self.y_hat_origin_point + np.array([0, -1.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)

