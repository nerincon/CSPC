# DEFINING THE SIMPLEST POSSIBLE CLASS

class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last)
print(user2.first, user2.last)


class Comment:
	def __init__(self, username, text, likes=0):
		self.username = username
		self.text = text
		self.likes = likes

c = Comment("davey123", "lol you're so silly", 3) 
another_comment = Comment("rosa77", "soooo cute!!!")
print(c.username, c.text, c.likes)
print(another_comment.username, another_comment.text, another_comment.likes)

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner) #Darcy
print(acct.balance) #0.0
print(acct.deposit(10))  #10.0
print(acct.withdraw(3))  #7.0
print(acct.balance)   #7.0


A User class with both a class attribute
class User:

	active_users = 0

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




print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user2.initials())
print(user1.initials())

print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)
user1.say_hi()

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
print(user2.logout())
print(User.active_users)


class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']
	def __init__(self, name, species):
		if species not in Pet.allowed
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species
	def set_species(self, species):
		if species not in Pet.allowed
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")


class Chicken:
	total_eggs = 0
	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.eggs = 0

	def lay_egg(self):
		self.eggs += 1
		Chicken.total_eggs += 1


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
print(Chicken.total_eggs) #0
c1.lay_egg()  #1
print(Chicken.total_eggs) #1
c2.lay_egg()  #1
c2.lay_egg()  #2
print(Chicken.total_eggs) #3


A User class with both a class attribute
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

	def __repr__(self):
		return f"{self.first} is {self.age}"

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




user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())

tom = User.from_string("Tom, Jones, 89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())

n = User("Nelson", "Rincon", 27)
print(type(n))
print(n)
n = str(n)
print(type(n))
print(n) # Both print same thing. __repr__ makes it readable. No need to turn it to a string


