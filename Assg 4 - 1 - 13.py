import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("white")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)  # Set speed to fastest
pen.hideturtle()
pen.penup()
pen.color("black")
pen.pensize(20)  # Font size

# Text to write
text = "when you leave because you are disgusted by me!"

# Spiral parameters
radius = 200
num_laps = 2
total_steps = 360 * num_laps  # Number of steps for two laps

# Calculate angle increment per step
angle_increment = 2 * math.pi / total_steps  # Radians per step

# Center of the screen
center_x = screen.window_width() // 2
center_y = screen.window_height() // 2

# Start at the outer edge
current_distance = radius
current_angle = 0

# Write text in a spiral
for char in text:
  # Calculate coordinates
  x = center_x + current_distance * math.cos(current_angle)
  y = center_y + current_distance * math.sin(current_angle)

  # Move pen to position
  pen.goto(x, y)
  pen.pendown()

  # Write character
  pen.write(char)

  # Update for next step
  current_angle += angle_increment
  current_distance -= 0.5  # Decrease distance slightly for inward spiral

# Keep the window open
screen.exitonclick()
