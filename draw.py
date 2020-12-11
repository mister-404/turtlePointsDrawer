import os
from Point import Point
from DrawData import DrawData
import turtle
import re

print(os.getcwd())
os.chdir(os.getcwd())

screen = turtle.Screen()
turt = turtle.Turtle()
turt.speed("fastest")
turtle.register_shape(os.getcwd() + "/imgs/wreathSmall.gif")
turt.shape(os.getcwd() + "/imgs/wreathSmall.gif")
turt.pensize(8)
SCALE = 20

drawSet = []

dataFile = open("./drawData.txt", 'r')
lines = dataFile.readlines()
points = []

for line in lines:
    line = line.strip()
    if line == "":
        drawSet.append(DrawData("black", points))
        points = []
    else:
        finder = re.findall("([-]?\d+)(?:,)[ ]?([-]?\d+)", line)
        xVal = float(finder[0][0])
        yVal = float(finder[0][1])
        points.append(Point(xVal, yVal))
drawSet.append(DrawData("black", points))

turtle.title("Christmas Penguin")

turt.penup()

for block in drawSet:
    turt.color("green")

    firstPoint = True

    for point in block.points:
        turt.goto(point.x * SCALE, point.y * SCALE)
        if firstPoint:
            firstPoint = False
            turt.pendown()

    turt.penup()

turt.home()

turt.color("red")
turt.goto(0, -500)
turt.write("Merry Christmas", True, "center",
           font=("Arial", 100, "normal", "bold", "underline"))
turt.goto(0, -200)

input('Press Enter to exit')
