import requests

session_cookie = 'MY_COOKIE' #todo change this
url = 'https://adventofcode.com/2023/day/1/input'

# Create a session object and set the session cookie
session = requests.Session()
session.cookies['session'] = session_cookie

# Make a GET request to fetch the input data
response = session.get(url)
sumTotal = 0
# Check if the request was successful (status code 200)
if response.status_code == 200:
    input_text = response.text
    for line in input_text.splitlines():
        if any(c.isdigit() for c in line):
            first_digit = next((c for c in line if c.isdigit()), 0)
            last_digit = next((c for c in reversed(line) if c.isdigit()), 0)
            print(line)
            print(first_digit+last_digit)
            concatenated_number = int(str(first_digit) + str(last_digit))
            sumTotal += concatenated_number
    print(sumTotal)
else:
    print(f"Failed to fetch input. Status code: {response.status_code}")
