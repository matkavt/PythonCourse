import turtle
# Вам предстоит написать свой язык программирования и компилятор!

# задание 1

def my_split(string):
	words = [""]
	for i in range(len(string)):
		if string[i] == " ":
			words.append("")
		else:
			words[-1] += string[i]
			print(string[i])
	print(words)

my_split("qwe qwe qwe")
print("qwe-qwe-qwe".split("-"))
print("-".join(["12", "12", "34", "555"]))

# напишите функцию, которая принимает текст программы вида "Вперёд n", "Назад n", "Влево n", "Вправо n"
# и запускает соответственно turtle.forward(n) и так далее
def run(command):
	words = command.split(" ")
	if words[0] == "Вперёд":
		turtle.forward(int(words[1]))
	elif words[0] == "Назад":
		turtle.backward(int(words[1]))
	elif words[0] == "Влево":
		turtle.left(int(words[1]))
	elif words[0] == "Вправо":
		turtle.right(int(words[1]))
	else:
		print("Неверная строка:", command)

# run("Вперёд 100")

# задание 2
# напишите функцию, которая по названию файла, открывает его и по очереди запускает стрки с помощью предыдущей функции
def execute(filename):
	file = open(filename, "r")
	for line in file:
		run(line)
	file.close()

execute("program.txt")

# задание 3
# обработайте все ошибки (несуществующий файл, неправильные комманды)

turtle.done()