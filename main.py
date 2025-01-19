from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)

is_race_on= False
user_input=screen.textinput(title="make a bet",prompt="which turtle do you think will win?:")

colours=["violet","indigo","blue","green","yellow","orange","red"]
y=-120
all_turtles=[]
for i in colours:
    timmy = Turtle(shape="turtle")
    all_turtles.append(timmy)
    timmy.penup()
    timmy.color(i)
    y+=40
    timmy.goto(-230,y)

if user_input:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_input:
                print("YOU WON!!")
            else:
                print("you lost, "+winning_colour+" won!!")
        random_dist=random.randint(0,10)
        turtle.forward(random_dist)


screen.exitonclick()