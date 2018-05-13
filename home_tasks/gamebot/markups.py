import telebot

def numbers():
	width = 5
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(*[str(j+1)+" 🔴" for j in range(width)])
	keyboard.row(*[str(j+1)+" 🔴" for j in range(width, 2*width)])
	keyboard.row(*[str(j+1)+" ⚫️" for j in range(width)])
	keyboard.row(*[str(j+1)+" ⚫️" for j in range(width, 2*width)])
	keyboard.row(*["🔴", "⚫️"])
	keyboard.row(*["1-5", "6-10"])
	keyboard.row(*["1-2", "3-4", "5-6", "7-8", "9-10"])
	return keyboard

def help():
	commands = ["/start", "/score" ,"/play"]
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	for cmd in commands:
		keyboard.row(cmd)
	return keyboard
