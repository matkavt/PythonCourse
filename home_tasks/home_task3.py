# Домашнее задание
# Сохраните файл data.json рядом с этим файлом и не трогайте следующие 8 строк
import json
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    for i in range(20):
        print("Не хватает файла с данными. (data.json)")
    assert(False)

# Дан объект data (как на лекции). (Верхние строчки его подгружают).
# На этот раз там 1000 записей
print(type(data))
print(len(data))
print(type(data[0]))
print(data[0])
print(data[0].keys())
print("___________")

# 1. Напишите функцию, которая считает среднюю зарплату
def avarage_salary(data):
    total_salary = 0
    for person in data:
        total_salary += person["money"]
    return total_salary / len(data)

# 2. Самое популярное имя
def common_name(data):
    my_dict = {}
    for person in data:
        name = person["name"]
        if name in my_dict:
            my_dict[name] += 1
        else:
            my_dict[name] = 1
            
    maximum = 0
    for key in my_dict:
        value = my_dict[key]
        if value > maximum:
            maximum = value
            result = key
    return result

# 3. Средний возраст
def avarage_age(data):
    total_age = 0
    for person in data:
        total_age += person["age"]
    return total_age / len(data)

# 4*. Доля автомобилей Kia в процентах (округлить до целого, функция round)
def kia_percent(data):
    kias = 0
    for person in data:
        car = person["car"]
        if car == "Kia":
            kias += 1
    return round(kias / len(data) * 100)

assert(avarage_salary(data) == 45018)
print("1 задание выполнено верно.")
assert(common_name(data) == "John")
print("2 задание выполнено верно.")
assert(avarage_age(data) >= 38 and avarage_age(data) <= 39)
print("3 задание выполнено верно.")
assert(kia_percent(data) == 36)
print("4 задание выполнено верно. Молодец!")
