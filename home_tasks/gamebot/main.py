import telebot
import markups
import engine
import users

token = "395971423:AAFj7EcbFIBKunM6yhlZk-fBHOWS6Hvy_SA"
bot = telebot.TeleBot(token)

help_text = """Угадывай числа и шарики и получай конфеты!
Доступные команды:
/start - регистрация
/score - посмотреть свой счёт
/play - играть!"""

@bot.message_handler(commands=["start"])
def f(message):
	name = message.from_user.first_name
	id = message.chat.id
	sweets = 10
	new_user = users.User(name, id, sweets)
	new_user.save()
	bot.send_message(message.chat.id, "Привет, {}! Вы зарегестрированы. У вас стартовый бонус - 10 конфет!".format(new_user.name))
	bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=["help"])
def f(message):
	markup = markups.help()
	bot.send_message(message.chat.id, help_text, reply_markup=markup)

@bot.message_handler(commands=["score"])
def f(message):
	user = users.get(message.chat.id)
	bot.send_message(message.chat.id, "У вас {} ({})".format("🍭"*user.sweets + "👺"*(-user.sweets), user.sweets))

@bot.message_handler(commands=["play"])
def f(message):
	markup = markups.numbers()
	bot.send_message(message.chat.id, "Выберите ставку", reply_markup=markup)

@bot.message_handler()
def f(message):
	engine.process(message, bot)

bot.polling()

# 1. Написать и запустить телеграм-бота-игру, используя втроенные кнопки (markup)

# Цель игры - отгадать число, которое загадал бот и шарик, который загадал бот.
# Есть варианты, например "10-20🔴"

# 2. За каждое угаданное число игрок получает конфету, а за не угаданное, лишается ее
# Добавьте базу данных, чтобы считать эти конфеты

# 3*. Для каждой "ставки" добавьте коэффицент. (Игрок должен получать больше конфет, если угадал само число, а не интервал)

# 4(***). Игрок должен сам выбирать, каким количеством конфет он рискует. 
# А также игрок получает конфеты за просмотр рекламы
