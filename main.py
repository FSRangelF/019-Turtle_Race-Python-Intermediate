from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
screen.title("Turtle Race")
bet = screen.textinput(title="Place Your Bet", prompt="Choose the color of the turtle: red/orange/yellow/green/blue/violet or indigo")

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
initial_y = [-90, -60, -30, 0, 30, 60, 90]

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=initial_y[turtle_index])
    turtles.append(new_turtle) 

finish = False
while not finish:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 230:
            if turtle.pencolor() == bet.lower():
                print(f"You Won! The {turtle.pencolor()} Turtle was the winner.")
            else:
                print(f"You Lost! The {turtle.pencolor()} Turtle was the winner.")
            finish = True

screen.exitonclick()
