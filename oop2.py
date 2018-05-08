class Animal:
	cool = True

	def make_sound(self, sound):
		print(f"Tjis animal says {sound}")

class Cat(Animal):
	pass


class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >=0:
			self._age = age
		else:
			self._age = 0

	def get_age(self):
		return self._age

	def set_age(self, new_age):
		if new_age >= 0:
			self._age = new_age
		else:
			self._age = 0

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("Age can't be negative!")
			# self._age = 0

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter #Not the best way to do this, but it works
	def full_name(self, name):
		self.first, self.last = name.split(" ")


jane = Human("Jane", "Goodall", 34)
print(jane.get_age())
jane.set_age(45)
print(jane.get_age())

print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"
print(jane.__dict__)


class Animal:

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def make_sound(self, sound):
		print(f"Tjis animal says {sound}")

	def __repr__(self):
		return f"{self.name} is a {self.species}"

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat")
		# Animal.__init__(self, name, species) #Better to go with super()
		self.breed = breed
		self.toy = toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue", "Scottish Fold", "String")
print(blue)
blue.play()


class User:

	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community"


u1 = User("Tom", "Garcia", 35)
u2 = User("Alberta", "Green", 45)
u3 = User("Liz", "Haussen", 25)
jasmine = Moderator("Jasmine", "O'connor", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'neil", 68, "Violin")
print(User.display_active_users())
print(Moderator.display_active_mods())



class Character:

	def __init__(self, name, hp, level):
		self.name = name
		self.hp = hp
		self.level = level

class NPC(Character):

	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)
	
	def speak(self):
		print("I heard there were monsters running around last night!")



class Aquatic:
	def __init__(self, name):
		self.name = name

	def swim(self):
		return f"{self.name} is swimming"
	def greet(self):
		return f"Iam {self.name} of the sea!"


class Ambulatory:
	def __init__(self, name):
		self.name = name

	def walk(self):
		return f"{self.name} is walking"

	def greet(self):
		return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
	def __init__(self, name):
		super().__init__(name=name)
		Aquatic.__init__(self, name=name) # you can also plug in the same line and take out super(). easier for others to understand



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")

Method resoultion order (3 ways) ------>

print(Penguin.__mro__)
print(Penguin.mro())
help(Penguin)

class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
 
 
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
 
 
class Child(Mother, Father):
    pass


person = Child()
print(person.hair_type)


from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"
	


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
print(j)
print(len(j))
triplets = j * 3
triplets[1].first = 'Jessica'
print(triplets)

# kevin and jessica have triplets!
triplets = (k + j) * 3
print(triplets)


class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data #even though data IS in dict, it returns False bc we told it to do so.

class Train():
    def __init__(self, num_cars):
    	self.num_cars = num_cars

    def __repr__(self):
    	return f"{self.num_cars} car train"
    	# return "{} car train".format(self.num_cars)

    def __len__(self):
    	return self.num_cars

a_train = Train(4)
print(a_train)  # 4 car train
print(len(a_train))  # 4

