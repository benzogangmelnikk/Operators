# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
left_bottom = simple_draw.get_point(0, 550)
right_top = simple_draw.get_point(100, 600)
for row in range(12):
    for column in range(12):
        simple_draw.rectangle(left_bottom, right_top, simple_draw.COLOR_DARK_ORANGE, width=2)
        left_bottom.x = left_bottom.x + 100
        right_top.x = right_top.x + 100
    left_bottom.y = left_bottom.y - 50
    right_top.y = right_top.y - 50
    if row % 2 == 0:
        left_bottom.x, right_top.x = -50, 50
    else:
        left_bottom.x, right_top.x = 0, 100

simple_draw.pause()
