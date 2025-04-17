import turtle


screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.tracer(0)

# Настройка черепашки
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Основные цвета
colors = ['gold', 'orange', 'darkorange', 'crimson']


# Функция рисования луча
def draw_ray(length, width):
    pen.begin_fill()
    for i in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.end_fill()


# Рисуем центральное солнце
pen.penup()
pen.goto(0, -40)
pen.pendown()
pen.color('gold')
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Рисуем лучи
for i in range(24):
    pen.color(colors[i % 4])

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(i * 15)  # 360°/24 = 15°
    pen.forward(40)
    pen.pendown()

    draw_ray(80, 10)  # Длина и ширина луча

    # Добавляем маленькие треугольники между лучами
    if i % 2 == 0:
        pen.penup()
        pen.forward(100)
        pen.pendown()
        pen.begin_fill()
        for i in range(3):
            pen.forward(20)
            pen.left(120)
        pen.end_fill()


pen.hideturtle()
screen.update()
screen.mainloop()
