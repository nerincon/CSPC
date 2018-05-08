#Custom For Loop

def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)


my_for([1,2,3,4,5], print)
my_for([1,2,3,4,5], square)

class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration


for x in Counter(50, 70):
	print(x)




REPEATED CODE FROM OTHER FILE --> ONLY ADDITION: __iter__


from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    # VERSION USING A GENERATOR FUNCTION 
    # def __iter__(self):
    #     for card in self.cards:
    #         yield card

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)



def week():
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	for day in days:
		yield day



days = week()
print(next(days))
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration


def yes_or_no():
	gen = ['yes', 'no']
	while True:
		for g in gen:
			yield g

# OR ---------

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"





gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 
print(next(gen)) 



def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1


counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


def make_song(count=99, beverage="soda"):
	for num in range(count, -1, -1):
		if num > 1:
			yield "{} bottles of {} on the wall".format(num, beverage)
		elif num == 1:
			yield "Only 1 bottle of {} left!".format(beverage)
		else:
			yield "No more {}!".format(beverage)





kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration

default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the wall.'



# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b) 
         a, b = b, a+b
     return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(1000000):
	print(n)



def get_multiples(number=1, count=10):
	new = number
	while count > 0:
		yield new
		new += number
		count -= 1



evens = get_multiples(2, 3)
print(next(evens)) # 2
print(next(evens)) # 4
print(next(evens)) # 6
print(next(evens)) # StopIteration

default_multiples = get_multiples()
print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# We can pass funcs as args to other funcs

def sum(n, func):
	total = 0
	for num in range(1,n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x


print(sum(3,cube))
print(sum(3,square))



from random import choice
# We can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())



from random import choice
# We can nest functions inside one another
def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg

	result = get_mood() + person
	return result

print(greet("Toby"))



############DECORATORS####################


#WITHOUT USING @ TO WRAP THE FUNCTION#
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Colt.")

def rage():
	print("I HATE YOU!")

# we are decorating our function 
# with politeness!
greet = be_polite(greet)

polite_rage = be_polite(rage)
polite_rage()


USING THE @ DECORATOR TO WRAP FUNCTION#

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
	print("I HATE YOU!")


greet()
rage()



# This version only accepts one argument
def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
	return "lol"

print(greet("todd"))
print(order(side="burger", main="fries"))
print(lol())


from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)



from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
    	print("Here are the args:", args)
    	print("Here are the kwargs:", kwargs)
    	return fn(*args, **kwargs)
    return wrapper




@show_args 
def do_nothing(*x, **y):
    pass


do_nothing(1, 2, 3,a="hi",b="bye")


# Should print (on two lines): 
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}


from functools import wraps


def double_return(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		val = fn(*args, **kwargs)
		return [val, val]
	return wrapper



@double_return 
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]



from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
    	if len(args) < 3:
    		return fn(*args)
    	else:
    		return "Too many arguments!"
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
	return sum(nums)



print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"



from functools import wraps

def only_ints(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
		if any([arg for arg in args if type(arg) != int]):
			return "Please only invoke with integers."
		return fn(*args)
	return inner

#####OR########(USING ISINSTANCE INSTEAD OF TYPE)


def only_ints(fn):
	@wraps(fn)
	def inner(*args, **kwargs):
		if any([arg for arg in args if isinstance(arg, int)]):
			return fn(*args)	
		return "Please only invoke with integers."
	return inner



@only_ints 
def add(x, y):
    return x + y
    
print(add(1, 2)) # 3
print(add("1", "2")) # "Please only invoke with integers."



from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(**kwargs):
    	is_admin = kwargs.get("role")
    	if is_admin == "admin":
    		return fn(**kwargs)
    	return "Unauthorized"
    return wrapper



@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"



print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"



# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)




from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'



def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable   
            newargs = []        
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)


# repeat_msg("hello", '5')
divide('1', '4')



from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
    	@wraps(fn)
    	def wrapper():#*args and **kwargs are not needed if no arguments will be needed when we call say_hi() at the end.
    	    print(f"Waiting {timer}s before running {fn.__name__}")
    	    sleep(timer)
    	    return fn()#*args and **kwargs are not needed if no arguments will be needed when we call say_hi() at the end.
    	return wrapper
    return inner



@delay(3)
def say_hi():
	return "hi"
    # print("hi") (if you want it to appear in the console)

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"



