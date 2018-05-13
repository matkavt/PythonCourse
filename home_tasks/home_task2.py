# Домашнее задание

# 2. Напишите функцию, которая принимает число и возвращает его модуль
def module(x):
    if x > 0:
        return x
    else:
        return -x

# 1. Напишите функцию, которая принимает 2 числа и возвращает True, если они отличаются не больше, чем на 10, иначе False
def near(a, b):
    return module(a-b) <= 10

# 3. Дан объект ivan. Напишите функцию, которая вернет его почтовый код
ivan = {
   "firstName": "Иван",
   "lastName": "Иванов",
   "address": {
       "streetAddress": "Московское ш., 101, кв.101",
       "city": "Ленинград",
       "postalCode": 101101
   },
   "phoneNumbers": [
       "812 123-1234",
       "916 123-4567"
   ]
}

def ivans_postal_code():
    d = ivan["address"]
    return d["postalCode"]

# 4. А теперь его второй номер телефона
def ivans_second_telephone_number():
    return ivan["phoneNumbers"][1]

# 5. Напишите функцию, которая создает массив из первых n натуральных чисел [1, 2, 3..n] и возвращает его
def first_n_numbers(n):
    numbers = []
    i = 0
    while i < n:
        numbers.append(i+1)
        i+=1
    return numbers

# 6*. Напишите функцию, которая возвращает массив из 20 первых чисел Фибоначчи (1, 1, 2, 3, 5, 8, 13 ...)
def fib20():
    numbers = [1,1]
    i = 0
    while i < 18:
        numbers.append(numbers[i]+numbers[i+1])
        i+=1
    return numbers

assert(near(35, -45) == False)
assert(near(-18, 28) == False)
assert(near(40, -19) == False)
assert(near(-38, -36) == True)
assert(near(22, 1) == False)
assert(near(41, -40) == False)
assert(near(43, -30) == False)
assert(near(-30, -48) == False)
assert(near(-16, -6) == True)
assert(near(17, -21) == False)
print("1 задание сделано верно")
assert(module(-20) == 20)
assert(module(-40) == 40)
assert(module(34) == 34)
assert(module(-41) == 41)
assert(module(24) == 24)
assert(module(4) == 4)
assert(module(-9) == 9)
assert(module(35) == 35)
assert(module(43) == 43)
assert(module(6) == 6)
print("2 задание сделано верно")
assert(ivans_postal_code() == 101101)
print("3 задание сделано верно")
assert(ivans_second_telephone_number() == "916 123-4567")
print("4 задание сделано верно")
assert(first_n_numbers(6) == [1, 2, 3, 4, 5, 6])
assert(first_n_numbers(40) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
assert(first_n_numbers(17) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
assert(first_n_numbers(24) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
assert(first_n_numbers(41) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
assert(first_n_numbers(23) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
assert(first_n_numbers(20) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
assert(first_n_numbers(1) == [1])
assert(first_n_numbers(34) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])
assert(first_n_numbers(41) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
print("5 задание сделано верно")
assert(fib20() == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765])
print("6 задание сделано верно. Молодец!")
