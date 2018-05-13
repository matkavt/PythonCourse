import telebot
token = "395971423:AAFj7EcbFIBKunM6yhlZk-fBHOWS6Hvy_SA"

bot = telebot.TeleBot(token)

e = " "*4

figures = "♚♛♜♝♞♟♔♕♖♗♘♙"

letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

chess = [
['♜','♞','♝','♛','♚','♝','♞','♜'],
['♟','♟','♟','♟','♟','♟','♟','♟'],
[e,e,e,e,e,e,e,e],
[e,e,e,e,e,e,e,e],
[e,e,e,e,e,e,e,e],
[e,e,e,e,e,e,e,e],
['♙','♙','♙','♙','♙','♙','♙','♙'],
['♖','♘','♗','♕','♔','♗','♘','♖']
]

def string_from(chess):
	return "\n".join(["".join(line) for line in chess])

def swap(command):
	first = command.split()[0]
	second = command.split()[1]
	from_x = letters[first[0]]
	from_y = int(first[1])
	to_x = letters[second[0]]
	to_y = int(second[1])
	figure = chess[8-from_y][from_x-1]
	chess[8 - to_y][to_x-1] = figure
	chess[8 - from_y][from_x-1] = e
	return chess

@bot.message_handler()
def f(message):
	swap(message.text)
	bot.send_message(message.chat.id, string_from(chess))

bot.polling()

