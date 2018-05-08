import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)


def censor(input):
	pattern = re.compile(r'\bfrack\w*\b', re.I)
	return pattern.sub("CENSORED", input)


print(censor("Frack you"))                #"CENSORED you"
print(censor("I hope you fracking die"))  #"I hope you CENSORED die"
print(censor("you fracking Frack"))      #"You CENSORED CENSORED"