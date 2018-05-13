def markup(labels):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard =True) #возвращает объект keyboard
    for label in labels:
        keyboard.add(telebot.types.KeyboardButton(label))
    return keyboard

import telebot
token = "ВАШ ТОКЕН"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=["image"])
def f2(message):
	image = open("your_image.jpg", "rb")
	bot.send_photo(message.chat.id, image)

@bot.message_handler()
def f(message):
	keyboard = markup(["/image", "Нет"])
	bot.send_message(message.chat.id, "Картинку?", reply_markup = keyboard)

bot.polling()