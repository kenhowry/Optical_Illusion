"""
Nested For Loops
This code creates an optical illusion containing a grid using nested loops.

File Name: howry_project_5.py
Author: Ken Howry
Date: 22.10.12
Course: COMP 1351
Assignment: Project V
Collaborators: N/A
Internet Source: N/A
"""

import dudraw

dudraw.set_canvas_size(500, 500)
dudraw.clear_rgb(228, 167, 250)
x_loc = 0
x_loc_2 = 500
y_loc = 0
y_loc_2 = 500

#vertical lines
for i in range(1):
    for j in range(21):
        dudraw.set_pen_color_rgb(252, 91, 228)
        dudraw.line(x_loc, y_loc, x_loc, y_loc_2)
        x_loc += 0.05

#horizontal lines
for i in range(1):
    for j in range(21):
        dudraw.line(x_loc, y_loc, x_loc_2, y_loc)
        x_loc = 0
        y_loc += 0.05

y_loc = 0

for i in range(21):
    for j in range(21):
        dudraw.set_pen_color_rgb(250, 220, 245)
        dudraw.filled_circle(x_loc, y_loc, 0.005)
        x_loc += 0.05
    y_loc += 0.05
    x_loc = 0

dudraw.show(float('inf'))