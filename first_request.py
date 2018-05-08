import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"Your request to {url} came back with status code {response.status_code}")

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data["joke"])

url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
	)

data = response.json()

print(data["results"])

#FINAL JOKES APPLICATION BELOW--------------------
import requests
from random import choice
user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term":user_input}
	).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one:")
	print(choice(results)['joke'])
elif num_jokes == 1:
	print(f"I found one about {user_input}. Here it is:")
	print(results[0]['joke'])
else:
	print(f"Sorry, couldn't find a joke with your term: {user_input}")