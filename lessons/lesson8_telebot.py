import telebot
import random
import requests
import json
# Это наш токен, который нам дал @BotFather
token = "ВАШ ТОКЕН"

# Создаём объект-бот, чтобы с нима работать
bot = telebot.TeleBot(token)

# Добавляем запись о сообщении в БД
def add_record(record):
	file = open("records.json", "r")
	data = json.load(file)
	file.close()
	data.append(record)
	file = open("records.json", "w")
	json.dump(data, file)
	file.close()

# Убираем команду (/price) из текста сообщения
def del_command(text_with_command):
	for i in range(len(text_with_command)):
		letter = text_with_command[i]
		if letter == " ":
			text = text_with_command[i+1:]
			return text
	return text_with_command

# def del_command(text):
# 	return " ".join(text.split()[1:])

# # Это - декоратор, с его помощью мы добавляем функции-слушатели
@bot.message_handler(commands=["start", "test"])
def get_message(message): # Имя не важно, аргумент должен быть - message
	# print(message) - печатается как словарь, но это не словарь
	add_record((message.chat.first_name, message.text))
	print(message.text)
	print(message.chat.id)
	bot.send_message(message.chat.id, "Привет, {}!".format(message.chat.first_name))

# функция получает цену валюты name
def get_value_of(name):
	link = "https://api.coinmarketcap.com/v1/ticker/?convert=RUB"
	data = requests.get(link).json()
	for item in data:
		if item["name"] == name:
			return item["price_rub"]

@bot.message_handler(commands=["ask"])
def get_message(message):
	add_record((message.chat.first_name, message.text))
	answers = ["Возможно", "Точно", "Никогда", "Обязательно", "Сложно сказать"]
	text = message.text
	if text[-1] == "?":
		# отвечаем
		bot.send_message(message.chat.id, random.choice(answers))
	else:
		bot.send_message(message.chat.id, "Задайте вопрос.")

@bot.message_handler(commands=["price"])
def f(message):
	add_record((message.chat.first_name, message.text))
	# text = " ".join(message.text.split()[1:])
	text = del_command(message.text)
	value = get_value_of(text)
	if value != None:
		bot.send_message(message.chat.id, "Курс {} сейчас {}₽".format(text, value))
	else:
		bot.send_message(message.chat.id, "Я не знаю такой криптовалюты")

bot.polling()