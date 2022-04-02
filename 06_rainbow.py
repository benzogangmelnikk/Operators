# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# x_start, y_start = 50, 50
# x_end, y_end = 350, 450
# start_point = sd.get_point(x_start, y_start)
# end_point = sd.get_point(x_end, y_end)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# for i in range(7):
#     sd.line(start_point, end_point, rainbow_colors[i], 4)
#     x_start = x_start + 5
#     x_end = x_end + 5
#     start_point = sd.get_point(x_start, y_start)
#     end_point = sd.get_point(x_end, y_end)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x, y = -50, -50
radius = 500
for i in range(7):
    sd.circle(sd.get_point(x, y), radius, rainbow_colors[i], 15)
    radius += 15

sd.pause()
