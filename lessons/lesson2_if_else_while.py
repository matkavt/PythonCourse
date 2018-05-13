# Булевый тип данных
True
False
a = True
b = False

# Операторы, уозвращающие булевый тип данных
print(2 > 0)#больше
print(2 < 0)#меньше
print(2 >= 0)#больше или равно (не меньше)
print(2 <= 0)#меньше или равно (не больше)
print(2 == 0)#равно ли?
print(2 != 0)#не равно ли?

# Операторы, для работы с булевым типом данных
# И
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# ИЛИ
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# НЕ
print(not True)
print(not False)

# Условие

if True:
    print("ok")

if False:
    print("Это не будет напечатано")

# Иначе
a = 20
if a > 0:
    print("а положительно")
else:
    print("a отрицательно или 0")

# Много условий
age = 20
if age > 90:
	print("Отдыхайте, дедушка")
elif age > 50:
	print("Посиди с внуками")
elif age > 24:
	print("Работай!")
elif age > 18:
	print("Учись, студент!")
elif age > 6:
	print("Учись, школьник!")
else:
	print("Мал еще")

# Цикл while
i = 0
while i < 20:
    print("на данном этапе переменная i равна", i)
    i += 1 # i = i + 1 (каждый раз увеличиваем i)
