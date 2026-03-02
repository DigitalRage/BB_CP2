#Import turtle, time, pillow, and random libraries
import turtle as t, time as T
def main():
    # Set up the drawing window
    screen = t.Screen()
    screen.tracer(1)
    t.speed(0)
    
    # function to check if user input is a valid choice between min and max values
    def choice_check(prompt, min_val, max_val):
        while True:
            choice = screen.textinput("Input", prompt)
            if choice.isdigit() and min_val <= int(choice) <= max_val:
                return int(choice)
    
    # function to check if user input is a valid color
    def color_check(prompt):
        while True:
            user_color = screen.textinput("Color", prompt)
            try:
                t.color(user_color)
                return user_color
            except t.TurtleGraphicsError:
                print("Please enter a valid color.")
    
    # Get user input for recursion depth, pen thickness, pen color, background color, and fill color
    recursion_depth = choice_check("What amount of recursion would you like to see? (0-5) ", 0, 5)
    t.pensize(choice_check("What pen thickness would you like? (1-10) ", 1, 10))
    t.color(color_check("What pen color would you like? (e.g. 'red', 'green', 'yellow') "))
    screen.bgcolor(color_check("What background color would you like? (e.g. 'black', 'white', 'blue') "))
    t.fillcolor(color_check("What fill color would you like? (e.g. 'red', 'green', 'yellow') "))
    
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
    recursive_triforce(0, 400, 1000, int(recursion_depth))
    T.sleep(10)