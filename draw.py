from Points import *
import turtle
import re

turt = turtle.Turtle()
turt.speed("fastest")
turt.hideturtle()
scale = 20

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
        turt.goto(point.x * scale, point.y * scale)
        if firstPoint:
            firstPoint = False
            turt.pendown()

    turt.penup()

turt.home()

input('Press Enter to exit')
