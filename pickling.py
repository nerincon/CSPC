import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)

# To unpickle something:
with open("pets.pickle", "rb") as file:
	zombie_blue = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())



###########################


import json

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
		
c = Cat("Charles", "Tabby")

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'

j = json.dumps(c.__dict__)
# results in '{"name": "Charles", "breed": "Tabby"}'




import jsonpickle

class Cat:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

c = Cat("Charles", "Tabby")

# To JSONPICKLE 'c' the cat:
with open("cat.json", "w") as file:
	frozen = jsonpickle.encode(c)
	file.write(frozen)

# To bring back 'c' the cat using JSONPICKLE
# with open("cat.json", "r") as file:
# 	contents = file.read()
# 	unfrozen = jsonpickle.decode(contents)
# 	print(unfrozen)




from csv import reader, writer

def update_users(old_firstname, old_lastname, new_firstname, new_lastname):
    with open("users.csv") as file:
    	csv_reader = reader(file)
    	rows = list(csv_reader)
    	count = 0

    with open("users.csv", "w") as file:
    	csv_writer = writer(file)
    	for row in rows:
    		if row[0] == old_firstname and row[1] == old_lastname:
    			print(row)
    			csv_writer.writerow([new_firstname, new_lastname])
    			count += 1
    		else:
    			print(row)
    			csv_writer.writerow(row)

    return "Users updated: {}".format(count)

print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0


from csv import reader, writer

def delete_users(firstname, lastname):
    with open("users.csv") as file:
    	csv_reader = reader(file)
    	rows = list(csv_reader)
    	count = 0

    with open("users.csv", "w") as file:
    	csv_writer = writer(file)
    	for row in rows:
    		if row[0] == firstname and row[1] == lastname:
    			count += 1
    		else:
    			csv_writer.writerow(row)

    return "Users updated: {}".format(count)

print(delete_users("Grace", "Hopper")) # Users deleted: 1.
print(delete_users("Colt", "Steele")) # Users deleted: 2.
print(delete_users("Not", "Here")) # Users deleted: 0.



