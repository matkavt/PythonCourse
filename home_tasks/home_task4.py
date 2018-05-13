# Домашнее задание

# import turtle
# import math
from tkinter import *

# # настройте цвет, размер черепашки и все такое
# def settings():
#     turtle.color("purple")
#     turtle.pensize(5)

# settings()

# # 1. Напишите функцию, которая черепашкой рисует шестиугольник
# # Сумма всех углов (внешних) в многоугольнике равна 360
# def hexagon():
#     for i in range(6):
#     	turtle.forward(100)
#     	turtle.right(360/6)
    
# # hexagon()

# # 2. Напишите функцию, которая черепашкой рисует любой n-угольник
# def polygon(n):
#     for i in range(n):
#     	turtle.forward(100)
#     	turtle.right(360/n)
        
# # for i in range(3,20):
# # 	polygon(i)

# # turtle.done()

# 3. Сделайте приложение Tkinter, которое будет "управлять" черепашкой
    # Пример - 4 кнопки: вперед, назад, вправо, влево.
    # Но вы можете проявить фантазию!
import turtle
def go_forward():
	turtle.forward(100)

def go_back():
	turtle.backward(100)

def left():
	turtle.left(30)

def right():
	turtle.right(30)

titles = ["Вперёд", "Назад", "Влево", "вправо"]
commands = [go_forward, go_back, left, right]

for i in range(4):
	my_button1 = Button()
	my_button1["text"] = titles[i]
	my_button1["command"] = commands[i]
	my_button1.pack()


# 4. Самое важное и сложное задание. Напишите какое-нибудь прикольное приложение на ткинтер на свой выбор
