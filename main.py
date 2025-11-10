from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
screen.title("Turtle Race")
bet = screen.textinput(title="Place Your Bet", prompt="Choose the color of the turtle: red/orange/yellow/green/blue/violet or indigo")

t_red = Turtle()
t_orange = Turtle()
t_yellow = Turtle()
t_green = Turtle()
t_blue = Turtle()
t_violet = Turtle()
t_indigo = Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
turtles = [t_red, t_orange, t_yellow, t_green, t_blue, t_violet, t_indigo]
initial_y = -180
index = 0
for turtle in turtles:
    turtle.shape("turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-240, y=initial_y)
    index += 1 
    initial_y += 60

finish = False
while not finish:
    index = 0
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 220:
            if colors[index] == bet.lower():
                print(f"You Won! The {colors[index]} Turtle was the winner.")
            else:
                print(f"You Lost! The {colors[index]} Turtle was the winner.")
            finish = True
        index += 1
screen.exitonclick()
