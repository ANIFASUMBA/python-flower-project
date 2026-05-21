import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower Drawing")

# Create the turtle
flower = turtle.Turtle()
flower.speed(0)  # Fastest speed
flower.color("white")
flower.width(2)
flower.hideturtle()


def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)


# Number of petals to draw
num_petals = 36
angle_step = 360 / num_petals

for i in range(num_petals):
    draw_petal(flower, 100, 60)  # Adjust radius and angle as needed
    flower.left(angle_step)  # Rotate for the next petal

# Keep the window open until closed by the user
screen.mainloop()