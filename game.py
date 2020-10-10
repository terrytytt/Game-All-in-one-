# step1 setting
import turtle
import random


window = turtle.Screen()
window.setup(width=800, height=800)

oscar = turtle.Turtle(shape="turtle")
terry = turtle.Turtle(shape="turtle")
tool = turtle.Turtle(shape="turtle")
oscar.color("red")
terry.color("yellow")
tool.color("blue")

# step2 Move turtle
# oscar (-350,100) ? (-350, -100) tool (300, 400)
oscar.penup()
terry.penup()
tool.penup()

oscar.goto(-350, 100)
terry.goto(-350, -100)
tool.goto(300, 400)

oscar.speed(10)
terry.speed(10)
tool.speed(10)

# step3 Draw a line
tool.pendown()
tool.goto(300,-400)

# step4 move!!!!!!
while True:
    if oscar.xcor() >= 300 or terry.xcor() >= 300:
        break
    oscar_value = random.randint(0,10)
    terry_value = random.randint(0,10)
    oscar.forward(oscar_value)
    terry.forward(terry_value)


