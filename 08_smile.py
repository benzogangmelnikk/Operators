# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile (x, y, color):
    point = simple_draw.get_point(x, y)
    # body
    simple_draw.circle(point, 40, color)
    # first eye
    simple_draw.circle(simple_draw.get_point(point.x - 15, point.y + 10), 5, color)
    # second eye
    simple_draw.circle(simple_draw.get_point(point.x + 15, point.y + 10), 5, color)
    # mouth
    point_list = [simple_draw.get_point(point.x - 18, point.y - 10), simple_draw.get_point(point.x - 10, point.y - 17),
                  simple_draw.get_point(point.x + 10, point.y - 17), simple_draw.get_point(point.x + 18, point.y - 10)]
    simple_draw.lines(point_list, color)


for _ in range(10):
    smile(random.randint(0, 600), random.randint(0, 600), simple_draw.COLOR_GREEN)
simple_draw.pause()
