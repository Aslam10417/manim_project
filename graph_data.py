from manim import *

class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[-5,5,1],y_range=[-3,3,1],
                    x_length = 10,y_length = 6,
                    axis_config = {"include_tip":False}
                    ).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label = "x",y_label="f(x)")
        graph = axes.plot(lambda x: x**0.5,x_range=[0,3],color=YELLOW)
        graph1 = axes.plot(lambda x: x,x_range=[0,3],color=GREEN_C)
        graphing_stuff = VGroup(axes,graph,graph1,axis_labels)

        self.play(DrawBorderThenFill(axes),Write(axis_labels))
        self.play(Create(graph))
        self.play(Create(graph1))
        # self.play(graphing_stuff.animate.shift(DOWN*1))
        # self.play(axes.animate.shift(LEFT*3),run_time=3)