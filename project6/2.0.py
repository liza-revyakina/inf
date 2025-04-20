from graphics import *
import time

win = GraphWin("Окно для графики", 400, 400)
win.setBackground('white')

# Начальные координаты автомобилей (начинаем справа)
x = [390, 400, 410]  # Начинаем с правой стороны окна
y = [100, 200, 300]


def car(x, y, color, flag):
    # Определяем точки для автомобиля
    body = Polygon(
        Point(x, y),
        Point(x + 50, y),  # Конец кузова
        Point(x + 50, y - 10),  # Лобовое стекло с правой стороны
        Point(x + 40, y - 20),
        Point(x + 30, y - 20),
        Point(x + 10, y - 10),
        Point(x, y - 10)
    )

    wheel1 = Circle(Point(x + 8, y + 4), 4)
    wheel2 = Circle(Point(x + 42, y + 4), 4)

    window = Polygon(
        Point(x + 20, y - 12),  # Начало лобового стекла
        Point(x + 36, y - 12),  # Конец лобового стекла
        Point(x + 36, y - 18),  # Верхняя точка лобового стекла
        Point(x + 30, y - 18)  # Верхняя точка лобового стекла
    )

    body.setOutline(color)
    body.setFill(color)
    wheel1.setFill("black")
    wheel2.setFill("black")
    window.setOutline("cyan")
    window.setFill("cyan")

    if flag == 1:
        body.draw(win)
        wheel1.draw(win)
        wheel2.draw(win)
        window.draw(win)

    if flag == 0:
        body.setOutline('white')
        body.setFill('white')
        wheel1.setFill("white")
        wheel1.setOutline('white')
        wheel2.setFill("white")
        wheel2.setOutline('white')
        window.setOutline("white")
        window.setFill("white")
        body.draw(win)
        wheel1.draw(win)
        wheel2.draw(win)
        window.draw(win)


# Изменяем цвет на 'blue' и задаем движение в противоположные стороны
for i in range(100):
    car(x[0], y[0], 'blue', 1)  # Первый автомобиль движется влево
    car(x[1], y[1], 'blue', 1)  # Второй автомобиль движется влево
    car(x[2], y[2], 'blue', 1)  # Третий автомобиль движется влево

    time.sleep(0.2)

    car(x[0], y[0], 'blue', 0)  # Убираем первый автомобиль
    car(x[1], y[1], 'blue', 0)  # Убираем второй автомобиль
    car(x[2], y[2], 'blue', 0)  # Убираем третий автомобиль

    x[0] -= 10  # Первый автомобиль движется влево
    x[1] -= 10  # Второй автомобиль движется влево
    x[2] -= 10  # Третий автомобиль движется влево

win.getMouse()
win.close()