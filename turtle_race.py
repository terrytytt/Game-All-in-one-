# step1 setting
import random
import turtle


class TurtleRace:
    """This is a game called turtle race"""

    def setup(self,width=800, height=800, end_x=300,
                 p1_color="red", p2_color="yellow",tool_color="green", bg_pic=False, bg_color="black"):
        """
        Setup with the property
        :param width:
        :param height:
        :param end_x:
        :param p1_color:
        :param p2_color:
        :param tool_color:
        :param bg_pic:
        :param bg_color:
        :return:
        """
        # set window
        window = turtle.Screen()
        if bg_pic:
            window.bgpic(bg_pic=bg_pic)
        window.bgcolor(bg_color)
        window.setup(width=width, height=height)
        self.window = window
        # set turtle
        self.p1 = turtle.Turtle(shape="turtle")
        self.p2 = turtle.Turtle(shape="turtle")
        self.tool = turtle.Turtle(shape="turtle")
        self.p1.color(p1_color)
        self.p2.color(p2_color)
        self.tool.color(tool_color)
        self.tool.hideturtle()
        self.p1.speed(0)
        self.p2.speed(0)
        self.tool.speed(0)
        self.end_x = end_x
        self.width = width
        self.height = height

    def start(self):
        """
        draw line and move turtle
        :return:
        """
        # step2 Move turtle
        # p1 (-350,100) ? (-350, -100) tool (300, 400)
        for pen in [self.p1, self.p2, self.tool]:
            pen.penup()
        start_x = -1*(self.width/2)
        self.p1.goto(start_x, 100)
        self.p2.goto(start_x, -100)
        self.tool.goto(self.end_x+10, self.height/2)

        # step3 Draw a line
        self.tool.pendown()
        self.tool.goto(self.end_x+10, -1*self.height/2)

    def run(self):
        """
        Run game
        :return:
        """
        self.setup()
        self.start()
        while True:
            if self.p1.xcor() >= self.end_x or self.p2.xcor() >= self.end_x:
                break
            p1_value = random.randint(0, 10)
            p2_value = random.randint(0, 10)
            self.p1.forward(p1_value)
            self.p2.forward(p2_value)
        self.window.exitonclick()

