import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to the fastest

# Function to draw a circle
def draw_circle():
    pen.circle(50)

# Function to draw a random zentangle pattern
def draw_zentangle():
    colors = ["green", "blue", "yellow"]  # Color palette
    while True:  # Keep drawing indefinitely
        for _ in range(36):  # Draw 36 circles for a full revolution
            pen.color(random.choice(colors))  # Randomly choose color
            # pen.fillcolor(random.choice(colors))  # Randomly choose fill color
            # pen.begin_fill()
            draw_circle()
            # pen.end_fill()
            pen.right(10)  # Rotate the turtle
        pen.color(random.choice(colors))  # Change the color for the next revolution
        # pen.fillcolor(random.choice(colors))  # Change fill color for the next revolution

# Hide the turtle and display the zentangle pattern
pen.hideturtle()
draw_zentangle()

# Keep the window open
screen.mainloop()
