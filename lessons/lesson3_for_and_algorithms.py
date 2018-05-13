# Занятие 3

# Цикл for
# 1
for i in range(0, 20, 1):# (start, end, step)
    print(i)
for i in range(0, 20):# (start, end, step=1)
    print(i)
for i in range(20):# (start=0, end, step=1)
    print(i)
# 2
for beetle in ["Paul", "John", "George", "Ringo"]:
    print("MEET", beetle + "!")
# 3
for letter in "Абырвалг":
    print(letter)

# Срез массива (или строки) и отрицательные индексы
array = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(array[0:5])
print(array[3:4])
print(array[2:7])
print(array[3:])
print(array[:3])
print(array[:-1])
print(array[-3])
print(array[:-5])
print(array[-6:-3])

# Рекурсия - функция вызывает саму себя
def summa(a, b):
    if a == 0:
        return b
    else:
        return 1 + summa(a-1, b)

print(summa(5,6))
print(summa(20,8))

# Полезные функции
usable_functions = [sum, abs, sorted, max, min, len, print]

for function in usable_functions:
    print(function)

# Немного про словарь
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
for key in my_dict:
    print(key)
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for item in my_dict.items():
    print(item)
