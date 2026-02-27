#Import turtle, time, pillow, and random libraries
import turtle as t, time as T, random as r
from PIL import Image

# Set up the drawing window
screen = t.Screen()
screen.tracer(1)
t.speed(0)

while True:
    choice = screen.textinput("Recursion Depth", "What amount of recursion would you like to see? (0-5) ")
    if choice.isdigit() and 0 <= int(choice) <= 10:
        break
    else: print("Please enter a valid number between 0 and 5.")
while True:
    thickness = screen.textinput("Pen Thickness", "What pen thickness would you like? (1-10) ")
    if thickness.isdigit() and 1 <= int(thickness) <= 10:
        t.pensize(int(thickness))
        break
while True:
    user_color = screen.textinput("Pen Color", "What pen color would you like? (e.g. 'red', 'green', 'yellow') ")
    try:
        t.color(user_color)
        break
    except t.TurtleGraphicsError:
        print("Please enter a valid color.")
while True:
    user_background = screen.textinput("Background Color", "What background color would you like? (e.g. 'black', 'white', 'blue') ")
    try:
        screen.bgcolor(user_background)
        break
    except t.TurtleGraphicsError:
        print("Please enter a valid color.")
while True:
    user_fill = screen.textinput("Fill Color", "What fill color would you like? (e.g. 'red', 'green', 'yellow') ")
    try:
        t.fillcolor(user_fill)
        break
    except t.TurtleGraphicsError:
        print("Please enter a valid color.")
# Draw a triangle of the given size at the given coordinates
def draw_triangle(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Function to do recursive drawing of the triforce pattern inside each triangle segment
def recursive_triforce(x, y, size, depth):
    if depth == 0:
        draw_triangle(x, y, size)
    else:
        new_size = size / 2
        recursive_triforce(x, y, new_size, depth - 1)
        recursive_triforce(x - new_size / 2, y - new_size * 0.866, new_size, depth - 1)
        recursive_triforce(x + new_size / 2, y - new_size * 0.866, new_size, depth - 1)

# Main program
t.clear()
recursive_triforce(0, 400, 1000, int(choice))
T.sleep(10)