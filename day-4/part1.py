file_path = "input.txt"

with open(file_path, "r") as file:
    data = file.read()

import re

rows = data.strip().split("\n")
total_worth = 0

for i in range(len(rows)):
    line_cleaned = re.sub(r'Card\s+\d+\s*:\s*', '', rows[i])
    lines_split = re.split('\| ', line_cleaned)
    lines_split[0] = lines_split[0].split(' ')
    lines_split[1] = lines_split[1].split(' ')
    arrays_without_empty_strings = [[x for x in arr if x != ''] for arr in lines_split]

    current_worth = 0  # Reset current_worth for each card

    # Iterate through each winning number in the first list
    for winning_card in arrays_without_empty_strings[0]:
        # Check if the winning number exists in your list of numbers
        if winning_card in arrays_without_empty_strings[1]:
            current_worth += 1

    total_worth += 2 ** (current_worth - 1) if current_worth > 0 else 0  # Calculate total worth for this card

print(total_worth)
