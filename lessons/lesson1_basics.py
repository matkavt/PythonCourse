# Это комментарий - строка, начинающаяся с решетки не является кодом
#Занятие 1

#Базовые типы данных (есть и другие)

# число
2
42
1092
# дробные числа записываются через точку
2.5
# строка
"Hello, world!"
'qwertyu'

# Операторы
1 + 1
9 - 4
-9
3 * 5
5 / 2
2**10 # возведение в степень
5 // 2 # деление нацело
5 % 2 # остаток от деления

# Переменные

x = 0
x = 5
x + 10
x*4
x-100
-x
x*x
x**2

d = 21
(d + 3) % 7

# Как лучше называть переменные
first_weekday_of_month = 3
current_day = 21
number_of_days_in_week = 7
current_weekday = (current_day + first_weekday_of_month - 1) % number_of_days_in_week
current_weekday

my_name = "Matvey"

# Конкатенация строк
my_name + my_name
"Привет, " + my_name + "!"

# Функции
def return_none():
  return None
# вызов функции
return_none()

# Функция с аргументом
def square(number):
      result = number*number
      return result

# вызов функции
square(42)

def say_hello_to(name):
    return "Hello, " + name + "!"

say_hello_to("Mat")

# Уже существующие функции (несколько)
abs(5)

# Вывод в консоль
print("sth")
print(12345678)
print(None)

# Ввод с клавиатуры
sth = input("Введите уже что нибудь: ")
print("Ваше что-нибудь - это: " + sth)


# запустить fn + f5 или Run -> Run Module
