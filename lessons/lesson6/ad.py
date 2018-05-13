import json
class Ad:
	text = None
	is_male = None
	price = None
	def __init__(self, text, is_male, price):
		self.text = text
		self.is_male = is_male
		self.price = price
	def show(self):
		print(self.text, "за", self.price, "₽")
	def get_from(dict):
		return Ad(
			text=dict["text"],
			is_male=dict["is_male"],
			price=dict["price"])
	def save(self):
		ad_dict = {"text": self.text, "is_male": self.is_male, "price": self.price}
		file = open("ads.json", "r")
		array = json.load(file)
		array.append(ad_dict)
		file.close()
		file = open("ads.json", "w")
		json.dump(array, file)
		file.close()

def get_ads():
	ads = []
	file = open("ads.json")
	array = json.load(file)
	for ad_dict in array:
		new_ad = Ad.get_from(ad_dict)
		ads.append(new_ad)
	file.close()
	return ads