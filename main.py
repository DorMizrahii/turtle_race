import turtle as t
import random
race_is_on = False
screen = t.Screen()
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
screen.setup(width=500, height=400)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -170
my_turtles = []
for i in range(6):
    x += 50
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x=-238, y=x)
    my_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in my_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You won! the winning turtle is {winning_color}.")
            else:
                print(f"You Lost! the winning turtle is {winning_color}.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
