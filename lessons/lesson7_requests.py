import requests

# Новости

class News:
	def __init__(self, dictionary):
		self.header = dictionary["header"]
		self.text = dictionary["text"]

	def __str__(self):
		return "------\n{}\n------\n{}\n".format(self.header, self.text)

def get_news(link):
	news = []
	data = requests.get(link).json()
	for dictionary in data:
		news.append(News(dictionary))
	return news

def main1():
	news = get_news("http://matkavt.host22.com/json/news.json")
	for item in news:
		print(item)

# Погода

def kelvin_to_celsius(temp):
    return temp-273.15

def round2(x):
	return round(x*100) / 100

def get_weather(city_name):
	link = "http://api.openweathermap.org/data/2.5/weather?q={}&apikey=9015826a4bfd2a4af7fe7fe0fc673f71".format(city_name)
	data = requests.get(link).json()
	t_kelvin = data["main"]["temp"]
	t_celsius = kelvin_to_celsius(t_kelvin)
	return round2(t_celsius)

def get_courses():
	link = "https://api.coinmarketcap.com/v1/ticker/?convert=RUB"
	response = requests.get(link)
	data = response.json()
	return data

def main2():
	while True:
		city = input()
		try:
			result = get_weather(city)
			print(result)
		except:
			print("Ошибка!")

def main3():
	data = get_courses()
	for item in data:
		print("{} вырос на {}% за 1 час".format(item["name"], item["percent_change_24h"]))

if __name__ == '__main__':
	main3()
	# main1()
	# main2()
