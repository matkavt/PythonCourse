link = "https://api.coinmarketcap.com/v1/ticker/?convert=RUB"

# создайте запрос и посмотрите, что лежит по этой ссылке.
import requests
data = requests.get(link).json()
print(type(data))
print(type(data[0]))
print(data[0].keys())

# 1. Выведите все Валюты и их цену в рублях
def print_all():
	for coin in data:
		print("{} стоит {} рублей.".format(coin["name"], coin["price_rub"]))
# print_all()

# 2. Выведите, на сколько каждая валюта выросла за последний час (в процентах)
def print_changes():
	for coin in data:
		print("{} вырос(ла) на {}%.".format(coin["name"], coin["percent_change_1h"]))
# print_changes()

# 3. Средняя стоимость всех валют
def avarage_price():
	s = 0
	for coin in data:
		s += float(coin["price_rub"])
	return s / len(data)
# print(avarage_price())

def avarage_price24():
	s = 0
	for coin in data:
		percents = float(coin["percent_change_24h"])
		k = (percents + 100) / 100
		current_price = float(coin["price_rub"])
		s += current_price / k
	return s / len(data)
# print(avarage_price24())

# 4. На сколько выросла средняя стоимость за 24 часа
def change24():
	return avarage_price() - avarage_price24()
# print(change24())

def avarage_price7d():
	s = 0
	for coin in data:
		percents = float(coin["percent_change_7d"])
		k = (percents + 100) / 100
		current_price = float(coin["price_rub"])
		s += current_price / k
	return s / len(data)

# 5*. Напишите функцию, которая принимает число рублей, а возвращает число рублей, которое вы бы заработали, если бы купили криптовалюту на эту сумму 7 дней назад
def count24(summa):
	price = avarage_price24()
	coins = summa / price
	new_price = avarage_price()
	new_summa = coins * new_price
	return new_summa

print(count24(100))
# print(len(data))
