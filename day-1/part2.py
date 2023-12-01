import requests
import re

session_cookie = 'MY_COOKIE' #todo change this
url = 'https://adventofcode.com/2023/day/1/input'

# Create a session object and set the session cookie
session = requests.Session()
session.cookies['session'] = session_cookie

# Make a GET request to fetch the input data
response = session.get(url)
sumTotal = 0

# Make hashmap to map word to letter
keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
values = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']
map_numbers = {k: v for k, v in zip(keys, values)}

def replace_words(text):
    for k, v in map_numbers.items():
        text = text.replace(k, v)
    return text

def calibration(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))
# Check if the request was successful (status code 200)
if response.status_code == 200:
    input_text = response.text
    for line in input_text.splitlines():
        line = calibration(replace_words(line))

        sumTotal += line
    print(sumTotal)
else:
    print(f"Failed to fetch input. Status code: {response.status_code}")
