from turtle import *
from random import random

for steps in range(200):
    for c in ('pink', 'brown', 'orange'):
        color(c)          # меняем цвет
        forward(steps)    # идём вперёд на `steps` пикселей
        right(60)        # поворот на 30° вправо
