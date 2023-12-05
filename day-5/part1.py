"""
Strategy : do not fill unmapped elements because absence of information means it's the same src and dest
seed_to_soil :
50 98 2
means soil seed length
"""

import re

file_path = "input-ex.txt"

with open(file_path, "r") as file:
    data = file.read()

lines = data.split("\n")
first_line = lines[0]

# 1) Get initial seeds into a list
numbers_list = re.findall(r'\d+', first_line)
numbers = list(map(int, numbers_list))

lines = lines[2::]

seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temp, temp_humidity, humidity_location = \
    {}, {}, {}, {}, {}, {}, {}

pattern_number = re.compile(r'\b\d+\b')
print(lines)

for i in range(len(lines)):
    # finding "headlines"
    if not pattern_number.search(lines[i]):
        headline = lines[i].split('-', 1)[0].strip()
        # treat each headline differently
    else:
        continue
print(numbers)
