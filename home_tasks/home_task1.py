# Домашнее задание

# 1. Напишите функцию, которая возвращает куб числа (число в третьей степени)
def cube(x):
    return None

# 2. Напишите функцию, которая принимает температуру в кельвинах и возвращает в цельсиях
def kelvin_to_celsius(temp):
    return None

# 3*. Напишите функцию, которая принимает коэффиценты (a, b, c) квадратного уравнения ax^2 + bx + c = 0 и возвращает его корни (решения)
# Решить эту задачу можно с помощью дискриминанта
# Вернуть 2 значения можно с помощью запятой ( return 1, 2 )
# Для упрощения тестируются только уравнения с двумя целыми решениями
def solve(a, b, c):
    #code
    return None, None

# Система проверки дз. Если тут не было ошибки, то все правильно
assert(cube(15) == 3375)
assert(cube(12) == 1728)
assert(cube(22) == 10648)
assert(cube(24) == 13824)
assert(cube(22) == 10648)
assert(cube(19) == 6859)
assert(cube(4) == 64)
assert(cube(17) == 4913)
assert(cube(16) == 4096)
assert(cube(25) == 15625)
print("1 задание сделано верно")
assert(kelvin_to_celsius(7) == -266)
assert(kelvin_to_celsius(324) == 51)
assert(kelvin_to_celsius(55) == -218)
assert(kelvin_to_celsius(7) == -266)
assert(kelvin_to_celsius(182) == -91)
assert(kelvin_to_celsius(269) == -4)
assert(kelvin_to_celsius(264) == -9)
assert(kelvin_to_celsius(396) == 123)
assert(kelvin_to_celsius(113) == -160)
assert(kelvin_to_celsius(321) == 48)
print("2 задание сделано верно")
assert(solve(1, 6, -7) == (1, -7) or solve(1, 6, -7) == (-7, 1))
assert(solve(2, -22, -24) == (12, -1) or solve(2, -22, -24) == (-1, 12))
assert(solve(1, -17, 30) == (15, 2) or solve(1, -17, 30) == (2, 15))
assert(solve(3, 0, -27) == (3, -3) or solve(3, 0, -27) == (-3, 3))
assert(solve(1, 25, -26) == (1, -26) or solve(1, 25, -26) == (-26, 1))
assert(solve(2, 12, 10) == (-1, -5) or solve(2, 12, 10) == (-5, -1))
assert(solve(2, -14, 12) == (6, 1) or solve(2, -14, 12) == (1, 6))
assert(solve(5, -25, 20) == (4, 1) or solve(5, -25, 20) == (1, 4))
assert(solve(1, -22, 0) == (22, 0) or solve(1, -22, 0) == (0, 22))
assert(solve(2, 8, 0) == (0, -4) or solve(2, 8, 0) == (-4, 0))
print("3 задание сделано верно")
