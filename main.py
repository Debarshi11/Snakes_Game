from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Gmae")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for positions in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(positions)





screen.exitonclick()