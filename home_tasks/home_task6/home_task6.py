# Домашнее задание
import math
import turtle
# 1. Напишите класс Point, у которого есть свойства x, y, color (строчка типа "red" или "green"), метод distance_to_other(point), который возвращает расстояние между двумя точками и метод __str__
class Point:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def distance_to_other(self, other_point):
		dx = abs(self.x - other_point.x)
		dy = abs(self.y - other_point.y)
		return math.sqrt(dx*dx + dy*dy)

	@staticmethod
	def distance_between_two_point(point1, point2):
		return point1.distance_to_other(point2)

	def __str__(self):
		return "Point({}, {})".format(self.x, self.y)

point = Point(0, 0, "red")
other_point = Point(30, 40, "black")
print(point)
assert(point.distance_to_other(other_point) == 50)
assert(Point.distance_to_other(point, other_point) == 50)
# print("Нормально!")

# 2. напишите класс Drawer, который с помошью черепашки умет рисовать круг, квадрат, треугольник
class Drawer:

	def draw_rect(self, side):
		for i in range(4):
			turtle.forward(side)
			turtle.left(90)

	def draw_triangle(self, side):
		for i in range(3):
			turtle.forward(side)
			turtle.left(120)

	def draw_circle(self, radius):
		d = 2*radius
		l = math.pi * d
		for i in range(360):
			turtle.forward(l/360)
			turtle.left(1)

# 3. Дополните класс Drawer функцией __str__, а так же функцией draw_point, которая рисует маленькую точку (квадрат 1 на 1) на координатах x, y. Не забудьте поменять цвет!
	def draw_point(self, point):
		turtle.color(point.color)
		turtle.up()
		turtle.goto(point.x, point.y)
		turtle.down()
		self.draw_rect(1)

# 4. Туда же напишите функцию draw_points(points), которая принимает список точек и рисует по очереди эти точки
	def draw_points(self, points):
		for point in points:
			self.draw_point(point)

drawer = Drawer()
# drawer.draw_rect(50)
# drawer.draw_triangle(50)
# drawer.draw_circle(50)
turtle.pensize(10)
# drawer.draw_point(Point(100, 100, "purple"))
# drawer.draw_points([Point(100, 100, "purple"), Point(-100, 50, "green")])
# Раскомментируйте, когда сделаете 4 задание)
# import smile 

# turtle.done()