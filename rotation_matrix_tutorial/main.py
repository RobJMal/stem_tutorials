from manim import *

class XHatVectorDerivation(Scene):
    def construct(self):
        self.show_circle()
        self.show_circle_axis()
        self.show_x_coodinate_axis()
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

    def show_x_coodinate_axis(self):
        self.x_coodinate_origin_point = np.array([-1, 2, 0])

        x_start = self.x_coodinate_origin_point + np.array([-1, 0, 0])
        x_end = self.x_coodinate_origin_point + np.array([7, 0, 0])

        y_start = self.x_coodinate_origin_point + np.array([0, 1.5, 0])
        y_end = self.x_coodinate_origin_point + np.array([0, -1.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_hat_axes_labels(self.x_coodinate_origin_point)

    def show_y_hat_axis(self):
        self.y_coordinate_origin_point = np.array([-1, -2, 0])

        x_start = self.y_coordinate_origin_point + np.array([-1, 0, 0])
        x_end = self.y_coordinate_origin_point + np.array([7, 0, 0])

        y_start = self.y_coordinate_origin_point + np.array([0, 1.5, 0])
        y_end = self.y_coordinate_origin_point + np.array([0, -1.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_hat_axes_labels(self.y_coordinate_origin_point)

    # Adds the labels for the x_hat and y_hat axes
    def add_hat_axes_labels(self, axes_origin_point):
        x_labels = [
            MathTex(r"\frac{\pi}{2}"), MathTex("\pi"),
            MathTex(r"\frac{3 \pi}{2}"), MathTex("2 \pi")
        ]

        y_labels = [MathTex("1"), MathTex("-1")]

        for i in range(len(x_labels)):
            x_labels[i].next_to(axes_origin_point + np.array([PI*(i+1)/2, 0, 0]), DOWN)
            self.add(x_labels[i])
        
        y_labels[0].next_to(axes_origin_point + np.array([0, 1, 0]), LEFT)
        y_labels[1].next_to(axes_origin_point + np.array([0, -1, 0]), LEFT)
        self.add(y_labels[0], y_labels[1])




