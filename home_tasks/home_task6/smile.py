from home_task6 import Point
from home_task6 import Drawer
import turtle

data = [
[0,0,0,0,0,0,0,0],
[0,1,1,0,0,1,1,0],
[0,1,1,0,0,1,1,0],
[0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0],
[0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,0,0,0,0,0]
]

points = []
for i in range(8):
	for j in range(8):
		if data[i][j] == 1:
			color = "red"
		else:
			color = "blue"
		point = Point(j*10, -i*10, color)
		points.append(point)
print(points)
turtle.speed(-1)
turtle.pensize(9)
Drawer().draw_points(points)
turtle.done()