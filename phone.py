import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
	    return match.group()
	return None


print(extract_phone("My number is 432 567-8976"))
print(extract_phone("My number is 432 567-897622"))
print(extract_phone("432 567-8976 sdfsgeag"))
print(extract_phone("432 567-8976"))


def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)


# print(extract_all_phones("My number is 432 567-8976 or call me at 544 433-9922"))
# print(extract_all_phones("My number is 432 56"))

# def is_valid_phone(input):
# 	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
# 	match = phone_regex.search(input)
# 	if match:
# 	    return True
# 	return False

#OR ------>

def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
	    return True
	return False

print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 ads"))
print(is_valid_phone("asd 432 567-8976 d"))


def is_valid_time(input):
	time_regex = re.compile(r'^\d\d?:\d{2}$')
	match = time_regex.search(input)
	if match:
		return True
	return False

print(is_valid_time("10:45"))       #True
print(is_valid_time("1:23"))        #True
print(is_valid_time("10.45"))       #False
print(is_valid_time("1999"))        #False
print(is_valid_time("145:23"))      #False


