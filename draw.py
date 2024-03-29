from Point import Point
from DrawData import DrawData
import turtle
import re

turt = turtle.Turtle()
turt.speed("fastest")
turt.hideturtle()
turt.pensize(8)
SCALE = 10

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
turt.goto(0, -200)
turt.write("Merry Christmas", True, "center",
           font=("Arial",  int(SCALE * 2), "normal", "bold", "underline"))

input('Press Enter to exit')
