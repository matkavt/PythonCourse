# Класс - новый тип данных
class NewType:
	pass

sth = NewType() #создание объекта класса
print(type(sth))

# Внутри класса могут быть переменные - свойства
class Point:
	x = 0
	y = 0

point = Point()
print(point.x)

# Внутри класса могут быть функции - методы
class Gun:
	def fire(self): # self - ссылка на тот объект, для которого вызван этот метод
		print("БАБАХ")

my_gun = Gun()
my_gun.fire() # == Gun.fire(gun)

# Конструктор класса - __init__ - помогает создать объект класса
class Contact:
	name = None # это можно здесь и не писать (написал просто так)
	phone_number = None # это можно здесь и не писать

	def __init__(self, name, phone_number):
		self.name = name
		self.phone_number = phone_number

	def __str__(self): # специальный метод, который автоматически вызовется при выводе объекта класса Contact
		return "Имя: "+self.name+", номер: "+self.phone_number

	def call(self):
		for letter in self.phone_number:
			if letter != "-":
				print(letter)
		print("Гудки")

	def rename(self, new_name):
		self.name = new_name

mary_contact = Contact("Mary", "8-800-555-35-35")
print(mary_contact) # == print(mary_contact.__str__())

mary_contact.call() # == print(Contact.call(mary_contact))
mary_contact.rename("Do not call!!") # == print(Contact.rename(mary_contact, "Do not call!!"))

print(mary_contact) # == print(mary_contact.__str__())

# Еще примерчик
class ContactBook:
	name = None
	contacts = [] # значение по умолчанию

	def __init__(self, name):
		self.name = name

	def add(self, contact):
		self.contacts.append(contact)

	def find_contact_by_name(self, name):
		for contact in self.contacts:
			if contact.name == name:
				return contact

	def remove_contact_named(self, name):
		contact = self.find_contact_by_name(name)
		self.contacts.remove(contact)

	def __str__(self):
		result = "Телефонная книга '" + self.name + "':\n"
		for contact in self.contacts:
			result += contact.__str__() + "\n"
		return result

contact1 = Contact("Mary", "8-999-99-99-99")
contact2 = Contact("Peter", "8-000-00-00-00")

book = ContactBook("Моя телефонная книга")
book.add(contact1)
book.add(contact2)

print(book)
print(book.find_contact_by_name("Mary"))
book.find_contact_by_name("Mary").call()
book.find_contact_by_name("Mary").rename("Сюда не звонить!")
print(book)
book.remove_contact_named("Peter")

print(book)
