import json

def from_dict(json_dict):
	return User(json_dict["name"], json_dict["id"], json_dict["sweets"])

def to_dict(user):
	return {"name": user.name, "id": user.id, "sweets": user.sweets}

def get(id):
	file = open("database.json", "r")
	users_dict = json.load(file)
	file.close()
	if str(id) in users_dict:
		user_dict = users_dict[str(id)]
		return from_dict(user_dict)
	else:
		return None

class User:
	def __init__(self, name, id, sweets):
		self.name = name
		self.id = id
		self.sweets = sweets

	def save(self):
		file = open("database.json", "r")
		users_dict = json.load(file)
		file.close()
		users_dict[str(self.id)] = to_dict(self)
		file = open("database.json", "w")
		users_dict = json.dump(users_dict, file)
		file.close()
