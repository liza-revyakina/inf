import turtle
import time


screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('lightgray')
screen.tracer(0)

# Создаем прямоугольник (красный)
rect = turtle.Turtle()
rect.color('red')
rect.penup()
rect.goto(-250, 100)
rect.pendown()
rect.hideturtle()

# Создаем треугольник (синий)
triangle = turtle.Turtle()
triangle.color('blue')
triangle.penup()
triangle.goto(-250, -100)
triangle.pendown()
triangle.hideturtle()


def draw_rect(t):
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()


def draw_triangle(t):
    t.begin_fill()
    for _ in range(3):
        t.forward(60)
        t.left(120)
    t.end_fill()


def movement_pattern():
    rect.setx(rect.xcor() + 2)
    triangle.setx(triangle.xcor() + 2)


# Основной цикл анимации
for i in range(280):
    rect.clear()
    triangle.clear()

    draw_rect(rect)
    draw_triangle(triangle)

    movement_pattern()

    screen.update()
    time.sleep(0.02)


screen.mainloop()
