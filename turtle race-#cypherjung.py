#turtle race
import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Racing Game-#cypherjung")
screen.bgcolor("white")

# Create the racing track
track = turtle.Turtle()
track.shape("square")
track.color("gray")
track.penup()
track.goto(-250, 200)
track.pendown()
track.right(90)
for _ in range(11):
    track.forward(400)
    track.penup()
    track.backward(400)
    track.left(90)
    track.forward(50)
    track.right(90)
    track.pendown()

# Create turtles
colors = ["red", "blue", "green", "orange", "purple"]
turtles = []
for i in range(len(colors)):
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.goto(-250, 170 - i * 50)
    turtle_obj.pendown()
    turtles.append(turtle_obj)

# User chooses a turtle
chosen_turtle = screen.textinput("Choose Your Turtle", "Enter the color of your turtle (red, blue, green, orange, purple): ")
chosen_turtle = chosen_turtle.lower()

# Check if the chosen turtle is valid
valid_turtle = False
for turtle_obj in turtles:
    if turtle_obj.color()[0].lower() == chosen_turtle:
        valid_turtle = True
        break

# Race the turtles
if valid_turtle:
    while True:
        for turtle_obj in turtles:
            distance = random.randint(1, 10)
            turtle_obj.forward(distance)
            if turtle_obj.xcor() >= 250:
                if turtle_obj.color()[0].lower() == chosen_turtle:
                    turtle_obj.penup()
                    turtle_obj.goto(0, 0)
                    turtle_obj.pendown()
                    turtle_obj.write("Congratulations! Your turtle wins!", align="center", font=("Arial", 20, "bold"))
                else:
                    turtle_obj.penup()
                    turtle_obj.goto(0, 0)
                    turtle_obj.pendown()
                    turtle_obj.write("Sorry, your turtle did not win.", align="center", font=("Arial", 20, "bold"))
                break
        else:
            continue
        break
else:
    print("Invalid turtle choice.")

# Exit on click
turtle.done()
exit()
