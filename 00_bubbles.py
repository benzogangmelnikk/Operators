# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# radius = 50

# for _ in range(3):
#   sd.circle(point, radius)
#   radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(x, y, radius, step, color=sd.COLOR_YELLOW):
    for _ in range(3):
        point = sd.get_point(x, y)
        sd.circle(point, radius, color)
        radius += step


# x = 100
# y = 100

# bubble(x, y, 50, 5)

# Нарисовать 10 пузырьков в ряд
# for i in range(10):
#   bubble(x, y, 50, 5)
#   x += 100

# Нарисовать три ряда по 10 пузырьков
# for rows in range(3):
#     for i in range(10):
#         bubble(x, y, 50, 5)
#         x += 100
#     y += 100
#     x = 100

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    x, y, step = random.randint(0, 1200), random.randint(0, 600), random.randint(1, 10)
    color = sd.random_color()
    bubble(x, y, 50, step, color)


sd.pause()
