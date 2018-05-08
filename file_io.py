# To write to a file, first open it in "w" mode
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# You can also write to files that don't yet exist
with open("lol.txt", "w") as file:
    file.write("haha" * 10000)

# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
	file.seek(0)
	file.write(":)\n")

# r+ read and write
with open("haiku.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
	file.write("HELLO!!!")




copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same

def copy(file_name, new_file_name):
    with open(file_name, "r") as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text)




copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt

def copy_and_reverse(file_name, new_file_name):
    with open(file_name, "r") as file:
        text = file.read()
    
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])


def statistics(file_name):
	with open(file_name, "r", encoding="utf-8-sig") as file:
		lines = file.readlines()

	return { "lines": len(lines),
	       "words": sum(len(line.split(" ")) for line in lines),
	       "characters": sum(len(line) for line in lines) }

print(statistics('story.txt'))


def find_and_replace(file_name, word, repl_word):
    with open(file_name, "r+", encoding="utf-8-sig") as file:
        filedata = file.read()
        filedata = filedata.replace(word, repl_word)
        file.seek(0)
        file.write(filedata)
        file.truncate()


find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,




# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
with open("fighters.csv") as file:
    data = file.read()

# Using reader # to iterate over it more than once, you need to turn it into a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file) #csv_reader = reader(file, delimiter="|")
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}") 

# Example where data is cast into a list
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data



from csv import writer, DictWriter
# Version using writer
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])


from csv import reader, writer
# using nested with statements
with open('fighters.csv') as file:
	csv_reader = reader(file) #data never converted to list
	with open('screaming_fighters.csv', "w") as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])


# Other approach, with only 1 file open at a time
with open('fighters.csv') as file:
	csv_reader = reader(file)
	# data converted to list and saved to variable
	fighters = [[s.upper() for s in row] for row in csv_reader]

with open('screaming_fighters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)



from csv import writer, DictWriter
# Version using writer
# with open("cats.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

# Version using DictWriter
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})



from csv import DictReader, DictWriter

def cm_to_in(cm):
	return float(cm) * 0.393701

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f["Height (in cm)"])
		})


add_user exercise
import csv
def add_user(firstname, lastname):
	with open("users.csv", "a") as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow([firstname, lastname])



add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johonson


from csv import reader

def print_users():
    with open("users.csv") as file:
    	csv_reader = reader(file)
    	next(csv_reader)
    	# print(f"{file[0]} {file[1]}")
    	for row in csv_reader:
    		print("{} {}".format(row[0], row[1]))

print_users() # None
# prints to the console:
# Colt Steele



from csv import reader

def find_user(firstname, lastname):
    with open("users.csv") as file:
    	csv_reader = reader(file)
    	for (index,row) in enumerate(csv_reader):
    		first_name_match = firstname == row[0]
    		last_name_match = lastname == row[1]
    		if first_name_match and last_name_match:
    			return index
    	return ("{} {} not found.".format(firstname, lastname))



print(find_user("Colt", "Steele"))# 1
print(find_user("Alan", "Turing")) # 3
print(find_user("Not", "Here")) # 'Not Here not found.'


