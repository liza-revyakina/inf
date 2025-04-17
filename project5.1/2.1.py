import turtle
import time


def moving_object(move, colour):
    move.fillcolor(colour)
    move.begin_fill()
    move.circle(30)
    move.end_fill()


screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('green')
screen.tracer(0)

# Первый круг (фиолетовый)
move = turtle.Turtle()
move.color('purple')
move.width(2)
move.penup()
move.goto(-250, 280)
move.pendown()
move.hideturtle()

# Второй круг (розовый)
second_move = turtle.Turtle()
second_move.color('pink')
second_move.width(2)
second_move.penup()
second_move.goto(250, -280)
second_move.pendown()
second_move.hideturtle()

for i in range(500):
    move.clear()
    second_move.clear()
    moving_object(move, 'purple')
    moving_object(second_move, 'pink')

    move.sety(move.ycor() - 2)
    second_move.sety(second_move.ycor() + 2)

    screen.update()
    time.sleep(0.02)

screen.mainloop()