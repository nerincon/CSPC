print("How many kilometers did you run today?");
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"You ran {miles} miles")

from random import randint
num = randint(1, 1000)

if num % 2 == 0:
    print("even")
else:
    print("odd")

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
else:
    print("yuck")

#=========================

print("How old are you?")

try:
	age = int(input())
except ValueError:
	age = None

if age is not None:
	if age >= 21:
		print("Drink, normal entry")
	elif age >= 18:
		print("You can enter but must get a wristbend")
	else:
		print("Too young, sorry")
else:
	print("Need to enter your age, please try again")




# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!!       
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /


if x > 0 and y > 0:
	print("both positive")
elif x < 0 and y < 0:
	print("both negative")
elif x > 0 and y < 0:
	print("x is positive and y is negative")
else:	
	print("y is positive and x is negative")


from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!


if actually_sick and sick_days > 0:
	calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
	calling_in_sick = True
else:
	calling_in_sick = False



from random import randint                           
x = randint(1, 3)

rock = 1
paper = 2
scissors = 3

print("rock (1)")
print("paper (2)")
print("scissors (3)")

try:
	p1 = int(input("enter player 1's choice (number from 1 - 3): "))
	if not (0 < p1 < 4):
		print("Not from choices provided, try again")
		quit()
except ValueError:
	p1 = None

p2 = x

print(f"Computer picked: {p2}")

if p1 is not None:
	if p1 == 1 and p2 == 3:
		print("player 1 wins")
	elif p1 == 2 and p2 == 1:
		print("player 1 wins")
	elif p1 == 3 and p2 == 2:
		print("player 1 wins")
	elif p1 == p2:
		print("No one wins")
	else:
		print("player 2 wins")
else:
	print("Please enter a number from 1-3 to play")


x = 0

for num in range(11,20,2):
	x+= num
print(x)

# OR------------

x = 0


for n in range(10, 21):
    if n % 2 != 0:
        x += n
print(x)


c = int(input("How many times do I have to tell you? "))

for n in range(c):
	print("Clean your room!")

for num in range(1, 21):
	if num == 4 or num == 13:
		print(f"{num} is UNLUCKY")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:
		print(f"{num} is odd")

for loop (inside another for loop)
for x in range(3):
	for smile in range(11):
		print("@"*smile)

while loop
smile2 = 1
while smile2 < 11:
	print("@"*smile2)
	smile2 += 1


print("Hey how's it going?  ")
msg = input()

while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN")



from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
	i += 1
	number = randint(1, 10)
	print(i)


from random import randint

random_number = randint(1,10)


while True:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess > random_number:
		print("Too high, please try again!")
	elif guess < random_number:
		print("Too low, please try again")
	else:
		print("You guessed it! You won!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break



ROCK PAPER SCISSOR GAME REFACTORED BY ADDING A LOOP AND OTHER

from random import randint                           #|  \



try:
	p1 = int(input("enter player 1's choice (number from 1 - 3): "))
	if not (0 < p1 < 4):
		print("Not from choices provided, try again")
		quit()
except ValueError:
	p1 = None

computer = None

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
	print("rock")
	print("paper")
	print("scissors")
	p1 = input("enter your choice: ").lower()
	if p1 == "quit" or p1 =="q":
		break
	computer = randint(1, 3)
	if computer == 1:
		computer = "rock"
	elif computer == 2:
		computer = "paper"
	else:
		Computer = "scissors"
	print(f"Computer picked: {computer}")
	if p1 == "rock" and computer == "scissors":
		player_wins += 1
		print("player 1 wins")
	elif p1 == "paper" and computer == "rock":
		player_wins += 1
		print("player 1 wins")
	elif p1 == "scissors" and computer == "paper":
		player_wins += 1
		print("player 1 wins")
	elif p1 == computer:
		print("No one wins")
	else:
		computer_wins += 1
		print("computer wins")

if player_wins == winning_score:
	print("CONGRATS, YOU WON!!")
elif player_wins == computer_wins:
	print("IT'S a FORFEIT!")
else:
	print("OH NO! THE COMPUTER WON...")

# Define my_stuff 
my_stuff = ["Car", 1, "Apartment", 1.0]
# Define nums 
nums = list(range(1, 99))

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

print("".join(sounds))

# result = ""
# for sound in sounds:
# 	result += sound.upper()
# 	print(result) 

names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(answer)

numbers = [1,2,3,4,5,6]
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

numbers1 = [1,2,3,4]
numbers2 = [3,4,5,6]

answer = [num for num in numbers1 if num in numbers2]
print(answer)

names = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in names]
print(answer2)

answer = [num for num in range(1, 101) if num % 12 == 0]
print(answer)

letters = "amazing"
answer = [letter for letter in letters if letter not in "aeiou"]

print(answer)


answer = [[i for i in range(0, 3)] for num in range(0, 3)]
print(answer)


answer = [[num for num in range(0,10)] for num in range(0,10)]
print(answer)

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(full_name)

DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH

# Using a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for v in donations.values():
    total_donations += v
print(total_donations)

This code picks a random food item:
from random import choice 
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!


bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock.keys():
	print(food)
	print(f"{bakery_stock.get(food)} left")
else:
	print(food)
	print("We don't make that")


game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = {}
stock_list.update(inventory)
print(stock_list)


# add the value 18 to stock_list under the key "cookie"
stock_list = {"cookie": 18}
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.update(inventory)
stock_list.pop("cake")
print(stock_list)
# OR-----------------------------------------
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')

# SPOTIFY DICTIONARY ACTIVITY BEGINS______________

playlist = {
"title": "patogonia bus",
"author": "colt steele",
"songs": [
	{"title": "song1","artist": ["blue"],"duration": 2.5},
	{"title": "song2","artist": ["kitty, djcat"],"duration": 5.25},
	{"title": "song3","artist": ["garfield"],"duration": 2.0}
	]
}

total_length = 0
for song in playlist["songs"]:
	total_length += song["duration"]
print(total_length)

# SPOTIFY DICTIONARY ACTIVITY ENDS______________



list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0, len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {thing[0]: thing[1] for thing in person}
OR
answer = {k:v for k,v in person}
OR
answer = dict(person)
print(answer)

answer = dict.fromkeys("aeiou", 0)
print(answer)


#GET THE ASCII CODES
answer = {count:chr(count) for count in range(65,91)}
print(answer)

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
	return [num for num in range(1,50) if num%2 == 0]
print(generate_evens())

def yell(something):
    return something.upper() +"!"
print(yell("go away"))

# Define speak below:
def speak(animal="dog"):
	if animal == "pig":
		return "oink"
	elif animal == "duck":
		return "quack"
	elif animal == "cat":
		return "meow"
	elif animal == "dog":
		return "woof"
	return "?"

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"


days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

def return_day(day):
	weekday = days.get(day)
	if weekday:
		return weekday
	return None

print(return_day(5))

#OR
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num < len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

OR
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None


def last_element(l):
    if l:
        return l[-1]
    return None
print(last_element(["hello", "goodbye", "imlast"]))


def number_compare(x,y):
	if x > y:
		return "First is greater"
	elif x < y:
		return "Second is greater"
	return "Numbers are equal"
print(number_compare(2,2))

def single_letter_count(string,letter):
	return string.lower().count(letter.lower())
print(single_letter_count("Hello World", "h"))
print(single_letter_count("Hello World", "z"))
print(single_letter_count("HelLo World", "l"))

def multiple_letter_count(string):
	return {letter:string.count(letter) for letter in string}
print(multiple_letter_count("awesome"))


def list_manipulation(mylist, command, location, value=None):
	if command == "remove" and location == "end":
		return mylist.pop()
	elif command == "remove" and location == "beginning":
		return mylist.pop(0)
	elif command == "add" and location == "beginning":
		mylist.insert(0,value)
		return mylist
	elif command == "add" and location == "end":
		mylist.insert(len(mylist),value)
		return mylist
	return "Argument not found"
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))

def is_palindrome(string):
	return string == string[::-1]:
print(is_palindrome("hannah"))
print(is_palindrome("testing"))

OR

def is_palindrome(string):
	stripped = string.replace(" ", "")
	return stripped == stripped[::-1]
print(is_palindrome("hannah hannah"))
print(is_palindrome("testing"))


def frequency(mylist, term):
	return mylist.count(term)
print(frequency(["n", "m", "k", "k"], "k"))
print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))

def multiply_even_numbers(numbers):
	product = 1
	for x in numbers:
		if x%2 == 0:
			product *= x
	return product
print(multiply_even_numbers([2,3,4,5,6]))


def capitalize(string):
	return string.upper()[:1] + string[1:]
print(capitalize("venezuela"))

def compact(l):
    return [val for val in l if val]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))

#OR 

def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals


def intersection(list1,list2):
	return [i for i in list1 if i in list2]
print(intersection([1,2,3], [2,3,4]))
print(intersection(['a','b','z'], ['x','y','z']))

def isEven(num):
    return num % 2 == 0

def partition(mylist, callback):
	trues = []
	falses= []
	for val in mylist:
		if callback(val):
			trues.append(val)
		else:
			falses.append(val)
	return [trues , falses]
print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
#OR 
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


def contains_purple(*args):
		if "purple" in args:
			return True
		return False

print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))
print(contains_purple("purple"))
print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))

def combine_words(word,**kwargs):
	if "prefix" in kwargs:
		return kwargs["prefix"] + word
	elif "suffix" in kwargs:
		return word + kwargs["suffix"]
	return word


print(combine_words("child"))  #'child'
print(combine_words("child", prefix="man"))  #'manchild'
print(combine_words("child", suffix="ish"))  #'childish'
print(combine_words("work", suffix="er"))  #'worker'
print(combine_words("work", prefix="home"))  #'homework'


# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

#code below:

result1 = count_sevens(1,4,7)
print(result1)
result2 = count_sevens(*nums)
print(result2)


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final



print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"


'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

cube = lambda num: num ** 3
print(cube(2))


def decrement_list(l):
	return list(map(lambda num: num-1, l))
print(decrement_list([1,2,3]))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


def remove_negatives(l):
	return list(filter(lambda val: val>=0, l))


print(remove_negatives([-1,0,3,4,-99]))

def is_all_strings(l):
	return all(type(val) == str for val in l)

print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2,'a', 'b', 'c']))
print(is_all_strings(('hello', 'goodbye')))


def extremes(l):
	return min(num for num in l), max(num for num in l)

#OR

def extremes(nums):
    return(min(nums), max(nums))

print(extremes([1,2,3,4,5]))
print(extremes((99,25,30,-7)))
print(extremes("alcatraz"))


def max_magnitude(l):
	return max(abs(num) for num in l)

print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))



def sum_even_values(*args):
	return sum(x for x in args if x % 2 == 0)


print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10))
print(sum_even_values(1))



def sum_floats(*args):
	return sum(arg for arg in args if isinstance(arg, float))
#OR
	# return sum(arg for arg in args if type(arg) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
print(sum_floats(1,2,3,4,5)) # 0


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)


def interleave(s1,s2):
	return "".join("".join(x) for x in (zip(s1,s2)))

print(interleave("lzr", "iad"))


def triple_and_filter(l):
    return [val*3 for val in l if val%4 == 0]
#OR
# return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(l):
	return list(map(lambda n: "{} {}".format(n["first"], n["last"]),l))


print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']



# Write a function called divide, which accepts two parameters (you can call them num1 and num2). 
#The function should return the result of num1 divided by num2. 
#If you do not pass the correct amount of arguments to the function, it should return the string 
#"Please provide two integers or floats". If you pass as the second argument a 0, 
#Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, 
#return the string "Please do not divide by zero"


def divide(num1, num2):
	try:
		total =  num1/num2
	except TypeError:
		return "Please provide two integers or floats"
	except ZeroDivisionError:
		return "Please do not divide by zero"
	return total
    Examples
    
    divide(4,2) // 2
    divide([],"1") // "Please provide two integers or floats"
    divide(1,0) // "Please do not divide by zero"


import keyword
def contains_keyword(*args):
	for item in args:
		if keyword.iskeyword(item):
			return True
	return False


print(contains_keyword("hello", "goodbye"))  #False
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  #True
print(contains_keyword("four", "for", "if"))  #True
print(contains_keyword("blah", "doggo", "crab", "anchor"))  #False
print(contains_keyword("grizzly", "ignore", "return", "False"))  #True


from termcolor import colored

text = colored("HI THERE!", color="cyan")
print(text)