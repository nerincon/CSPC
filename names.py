import re
def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

print(parse_name("Mrs. Tilda Swinton"))



def parse_date(input):
	date_regex = re.compile(r'^(?P<day>\d\d)[,/.](?P<month>\d\d)[,/.](?P<year>\d{4})$')
	match = date_regex.search(input)
	if match:
		return {
			"d": match.group("day"),
			"m": match.group("month"),
			"y": match.group("year"),
		}
	return None



print(parse_date("01/22/1999")) # {'d': '01', 'm': '22', 'y': '1999'}
print(parse_date("12,04,2003"))  #{'d': '12', 'm': '04', 'y': '2003'}
print(parse_date("12.11.2003"))  #{'d': '12', 'm': '11', 'y': '2003'}
print(parse_date("12.11.200312")) #None