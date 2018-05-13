# file = open("file.txt", "w")
# file.write("Hello, file!")
# file.close()

# with open("file.txt", "r") as file:
# 	content = file.read()
# 	print(content)

# def get_score():
# 	try:
# 		file = open("score.txt", "r")
# 		score = int(file.read())
# 		file.close()
# 		return score
# 	except:
# 		file = open("score.txt", "w")
# 		file.write("0")
# 		return 0

# def set_score(score):
# 	file = open("score.txt", "w")
# 	file.write(str(score))
# 	file.close()

import json
import random

def save(info):
	file = open("config.json", "w")
	json.dump(info, file)
	file.close()

def get_info():
	try:
		file = open("config.json", "r")
		info = json.load(file)
		file.close()
		return info
	except:
		start_info = {}
		save(start_info)
		return start_info

def win():
	info = get_info()
	name = input("Как вас зовут? ")
	if name in info:
		info[name] += 1
		print(name, "победил!")
		print("Ваш рейтинг: ", info[name])
	else:
		info[name] = 1
		print("Да вы у нас новый ползьзователь!")
		print("Ваш рейтинг: ", info[name])
	save(info)

def loose():
	info = get_info()
	name = input("Как вас зовут? ")
	if name in info:
		info[name] -= 1
		print(name, "проиграл!")
		print("Ваш рейтинг: ", info[name])
	else:
		info[name] = -1
		print("Да вы у нас новый ползьзователь!")
		print("Ваш рейтинг: ", info[name])
	save(info)

def loop():
	print("Выберите камень, ножницы или бумагу")
	user = input()
	if user == "Камень":
		computer = random.randint(1,3)
		if computer == 1:
			print("А у меня ножницы!")
			win()
		elif computer == 2:
			print("А у меня камень!")
			print("Ничья")
		else:
			print("А у меня бумага!")
			loose()
	elif user == "Ножницы":
		computer = random.randint(1,3)
		if computer == 1:
			print("А у меня бумага!")
			win()
		elif computer == 2:
			print("А у меня ножницы!")
			print("Ничья")
		else:
			print("А у меня камень!")
			loose()
	else:#бумага
		computer = random.randint(1,3)
		if computer == 1:
			print("А у меня камень!")
			win()
		elif computer == 2:
			print("А у меня бумага!")
			print("Ничья")
		else:
			print("А у меня ножницы!")
			loose()

def main():
	while True:
		loop()

if __name__ == '__main__':
	main()