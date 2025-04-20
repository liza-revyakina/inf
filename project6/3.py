from graphics import *
import time

# Создаем окно
win = GraphWin("Анимация автомобилей", 600, 400)
win.setBackground('lightblue')


# Функция для рисования автомобиля
def draw_car(x, y, color):
    body = Rectangle(Point(x, y), Point(x + 50, y - 20))
    body.setFill(color)
    body.draw(win)

    wheel1 = Circle(Point(x + 10, y), 10)
    wheel1.setFill("black")
    wheel1.draw(win)

    wheel2 = Circle(Point(x + 40, y), 10)
    wheel2.setFill("black")
    wheel2.draw(win)


# Начальные координаты автомобилей
car1_x = 0
car2_x = 550

# Основной цикл анимации
while True:
    # Очищаем окно
    win.delete("all")

    # Рисуем дорогу
    road = Rectangle(Point(0, 200), Point(600, 400))
    road.setFill("gray")
    road.draw(win)

    # Рисуем автомобили
    draw_car(car1_x, 350, "red")   # Первый автомобиль (движется вправо)
    draw_car(car2_x, 250, "blue")  # Второй автомобиль (движется влево)

    # Обновляем позиции автомобилей
    car1_x += 5   # Первый автомобиль движется вправо
    car2_x -= 5   # Второй автомобиль движется влево

    # Проверяем границы окна и меняем направление движения
    if car1_x > win.getWidth():   # Если первый автомобиль выходит за правую границу
        car1_x = -50               # Возвращаем его на левую сторону

    if car2_x < -50:               # Если второй автомобиль выходит за левую границу
        car2_x = win.getWidth()   # Возвращаем его на правую сторону

    time.sleep(0.05)               # Задержка для плавности анимации


# Закрываем окно при клике мыши (не будет достигнуто в этом примере)
win.getMouse()
win.close()
