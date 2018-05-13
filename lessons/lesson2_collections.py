# Кортеж, tuple (просто несколько значений)
# Редко используется. В основном для того, чтобы вернуть 2-3 значения из функции
pointA = (0, 1)
pointB = (20, 30)
# Достаем элемент по индексу
print(pointB[0])
print(pointB[1])

# Список, list (чаще массив, array)
# Используется, чтобы хранить список данных по порядку

numbers = [0,1,2,3,4,5,6,7,8,9]
student_names = ["Maxim", "Marine", "Anna", "Anya", "Elena", "Sofia"]

print(numbers[0])
print(numbers[5])
print(student_names[0])
print(student_names[2])

# Добавить элемент
student_names.append("Jane")

# Поменять элемент
numbers[0] = 42

# Крутая функция len - показывает размер списка, словаря или строки
print(len(numbers))
print(len(student_names))
print(len("qwerty"))

# Словарь много пар(ключ - значение)
capitals = {"Russia": "Moscow", "England": "London", "Germany": "Berlin"}

# Достаем элемент по ключу
print(capitals["Russia"])
print(capitals["England"])
print(capitals["Germany"])

# Добавляем элемент по ключу (или изменяем)
capitals["Italy"] = "Rome"

# Часто встречается вот такое
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
