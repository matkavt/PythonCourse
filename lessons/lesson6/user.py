import json
class User:
	name = None
	age = None
	is_male = None
	def __init__(self, name, age, is_male):
		self.name = name
		self.age = age
		self.is_male = is_male
	def dict(self):
		return {"name": self.name, "age": self.age, "is_male": self.is_male}
	def save(self):
		file = open("users.json", "r")
		data = json.load(file)
		data.append(self.dict())
		file.close()
		file = open("users.json", "w")
		json.dump(data, file)
		file.close()
	def get_dict_by(index):
		file = open("users.json", "r")
		data = json.load(file)
		user = data[index]
		file.close()
		return user
	def get_user_from_dict(dict):
		return User(
			name=dict["name"],
			age=dict["age"],
			is_male=dict["is_male"])
	def get_by(index):
		dict = User.get_dict_by(index)
		return User.get_user_from_dict(dict)
	def __str__(self):
		return "Person "+self.name

def new_user_from_input():
	name = input("Как вас зовут?: ")
	age = int(input("Сколько вам лет?: "))
	is_male = input("Напишите ДА, если вы мужчина: ") == "ДА"
	return User(name, age, is_male)