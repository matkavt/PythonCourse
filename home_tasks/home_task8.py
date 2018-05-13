import telebot
import requests

# 1. Написать и запустить телеграм-бота, который читает ваше сообщение наоборот
token = "395971423:AAFj7EcbFIBKunM6yhlZk-fBHOWS6Hvy_SA"
bot = telebot.TeleBot(token)


# def reverse_text(text):
# 	reversed_text = ""
# 	for i in range(0, len(text)):
# 		reversed_text = text[i] + reversed_text
# 	return reversed_text

def remove_first_word(text):
	words = text.split(" ")
	return " ".join(words[1:])

# handler
@bot.message_handler(commands=["weather"])
def f(message):
	city_name = remove_first_word(message.text)
	link = "https://api.openweathermap.org/data/2.5/weather?q={}&apiKey=9015826a4bfd2a4af7fe7fe0fc673f71".format(city_name)
	response = requests.get(link)
	data = response.json()
	bot.send_message(message.chat.id, str(int(data["main"]["temp"])-273))

# 2. Написать бота, который понимает команду /weather {city} и отправляет вам погоду в городе city
# https://api.openweathermap.org/data/2.5/weather?q={}&apiKey=9015826a4bfd2a4af7fe7fe0fc673f71

# 3*. Запоминать, в каком городе пользователь чаще всего справшивает погоду
# выводить погоду в этом городе по умолчанию (по команде /weather) (city = "")


bot.polling()