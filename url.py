import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())



def parse_bytes(input):
	binary_regex = re.compile(r'\b\d{8}\b')
	results = binary_regex.findall(input)
	return results



print(parse_bytes("11010101 101 323"))    # ['11010101']
print(parse_bytes("my data is: 10101010 11100010"))    # ['10101010', '11100010']
print(parse_bytes("asdsa"))   # []