import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')
screen.tracer(0)

# Параметры
total_rays = 24
base_ray_length = 80
ray_width = 10
triangle_size = 20
sun_radius = 40

colors = ['gold', 'orange', 'darkorange', 'crimson']

# Создаем черепашку для солнца
sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)


# Класс для луча с "дыханием"
class Ray:
    def __init__(self, index):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.width(2)
        self.index = index
        self.base_angle = index * 15
        self.color = colors[index % len(colors)]

        # Амплитуда изменения длины (растяжение)
        self.length_amplitude = random.uniform(10, 20)

        # Частота дыхания (колебаний в секунду)
        self.length_frequency = random.uniform(0.3, 0.7)

        # Фаза, чтобы лучи не дышали синхронно
        self.phase = random.uniform(0, 2 * math.pi)

    def draw(self, center_x, center_y, t):
        # Рассчитываем текущую длину с "дыханием"
        length_offset = self.length_amplitude * math.sin(2 * math.pi * self.length_frequency * t + self.phase)

        current_length = base_ray_length + length_offset

        angle = self.base_angle

        pen = self.turtle
        pen.clear()

        pen.penup()

        # Перемещаемся в центр солнца + смещение по координатам центра рисунка
        pen.goto(center_x, center_y)

        pen.setheading(angle)

        pen.forward(sun_radius)  # отступ от центра солнца

        pen.pendown()

        pen.color(self.color)

        # Рисуем прямоугольный луч с текущей длиной и шириной ray_width
        pen.begin_fill()

        for _ in range(2):
            pen.forward(current_length)
            pen.left(90)
            pen.forward(ray_width)
            pen.left(90)

        pen.end_fill()

        # Если индекс четный — рисуем треугольник на конце луча (с учетом текущего угла и длины)
        if self.index % 2 == 0:
            pen.penup()
            pen.forward(current_length + ray_width)
            pen.pendown()
            pen.begin_fill()
            for _ in range(3):
                pen.forward(triangle_size)
                pen.left(120)
            pen.end_fill()


# Создаем все лучи
rays = [Ray(i) for i in range(total_rays)]

# Параметры движения всего рисунка (солнце + лучи) по экрану — например, синусоида по X и Y
move_amplitude_x = 120  # пикселей по X
move_amplitude_y = 80  # пикселей по Y
move_frequency_x = 0.15  # колебаний в секунду по X
move_frequency_y = 0.2  # колебаний в секунду по Y


def animate(frame=0):
    t = frame / 30.0  # время в секундах (если ~30 FPS)

    # Смещение всего рисунка:
    offset_x = move_amplitude_x * math.sin(2 * math.pi * move_frequency_x * t)
    offset_y = move_amplitude_y * math.sin(2 * math.pi * move_frequency_y * t)

    sun.clear()
    sun.penup()
    sun.goto(offset_x, offset_y - sun_radius)
    sun.pendown()
    sun.color('gold')
    sun.begin_fill()
    sun.circle(sun_radius)
    sun.end_fill()

    for ray in rays:
        ray.draw(offset_x, offset_y, t)

    screen.update()

    screen.ontimer(lambda: animate(frame + 1), int(1000 / 30))  # ~30 FPS


animate()

screen.mainloop()
