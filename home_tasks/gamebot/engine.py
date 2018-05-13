import random
import users

def random_pair():
	return (random.randint(1,10), random.choice(["🔴", "⚫️"]))

def compare(first, second):
	return first[0] == second[0] and first[1] == second[1]

def check(pair, array):
	number = pair[0]
	return number in array

def get_type(text):
	components = text.split()
	if len(components) == 2 and components[0].isdigit() and components[1] in ["🔴", "⚫️"]:
		return 1
	components = text.split("-")
	if len(components) == 2 and components[0].isdigit() and components[1].isdigit():
		return 2
	if text in ["⚫️", "🔴"]:
		return 3
	return 0

def get_pair(text):
	components = text.split()
	return (int(components[0]), components[1])

def interval(text):
	components = text.split("-")
	return [i for i in range(int(components[0]), int(components[1])+1)]

def process(message, bot):
	type = get_type(message.text)
	result = random_pair()
	bot.send_message(message.chat.id, "Выпало {} {}".format(*result))
	if type == 1:
		pair = get_pair(message.text)
		if compare(pair, result):
			win(bot, message.chat.id)
		else:
			loose(bot, message.chat.id)
	elif type == 2:
		array = interval(message.text)
		if check(result, array):
			win(bot, message.chat.id)
		else:
			loose(bot, message.chat.id)
	elif type == 3:
		if message.text == result[1]:
			win(bot, message.chat.id)
		else:
			loose(bot, message.chat.id)
	else:
		bot.send_message(message.chat.id, "Некорректная ставка")

def win(bot, id):
	user = users.get(id)
	user.sweets += 1
	user.save()
	bot.send_message(id, "Вы выиграли, у вас теперь {} ({})".format("🍭"*user.sweets + "👺"*(-user.sweets), user.sweets))

def loose(bot, id):
	user = users.get(id)
	user.sweets -= 1
	user.save()
	bot.send_message(id, "Вы проиграли, у вас теперь {} ({})".format("🍭"*user.sweets + "👺"*(-user.sweets), user.sweets))
