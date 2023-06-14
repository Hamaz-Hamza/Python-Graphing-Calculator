
# Initialization and setup
import turtle
from math import *

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
x_axes = 600
y_axes = 300

# The x and y axes
t.pensize(3)
t.penup()
t.setpos(-x_axes, 0)
t.pendown()
t.setpos(x_axes, 0)
t.penup()
t.setpos(0, -y_axes)
t.pendown()
t.setpos(0, y_axes)

# The Grid
t.pensize(1)

y = y_axes
for i in range(11):
    t.penup()
    t.setpos(-x_axes, y)
    t.pendown()
    t.setpos(x_axes, y)
    step = y_axes/5
    y -= step

x = x_axes
for i in range(11):
    t.penup()
    t.setpos(x, y_axes)
    t.pendown()
    t.setpos(x, -y_axes)
    step = x_axes/5
    x -= step

# Graphing program
t.penup()

# User Input
x_range = float(turtle.textinput("User Input","Enter domain [-x,x]:"))
y_range = float(turtle.textinput("User Input","Enter range [-y,y]:"))
equation = turtle.textinput("User Input","Enter function equation in a form that is understandable by the computer (e.g. for x²+2x enter x**2 + x*2)\nDon't enter a non-function or a function with a vertical asymptote.")

# Graph endponts
t.setpos(-x_axes-30, 0)
t.write(-x_range)
t.setpos(x_axes+10, 0)
t.write(x_range)
t.setpos(0, -y_axes-20)
t.write(-y_range)
t.setpos(0, y_axes+10)
t.write(y_range)

# The Graph
x_multiplier = x_range/x_axes   # For scaling the output graph according to user input with respect to originally set x-axis value
y_multiplier = y_axes/y_range   # For scaling the output graph according to user input with respect to originally set y-axis value
t.color('red')
t.pensize(2)

for i in range(-x_axes, x_axes+1):
    x = i * x_multiplier
    y = eval(equation)
    y = y * y_multiplier
    if y < -y_axes or y > y_axes: continue
    t.setpos(i, y)
    t.pendown()
    
input()

        


    
    

