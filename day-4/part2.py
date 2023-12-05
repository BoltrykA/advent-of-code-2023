import re

file_path = "input.txt"

with open(file_path, "r") as file:
    data = file.read()

rows = data.strip().split("\n")
dict_of_copies = {}

for index in range(len(rows)):
    dict_of_copies[index] = dict_of_copies.get(index, 0) + 1
    if index == (len(rows)-1):
        break
    line_cleaned = re.sub(r'Card\s+\d+\s*:\s*', '', rows[index])
    lines_split = re.split('\| ', line_cleaned)
    lines_split[0] = lines_split[0].split(' ')
    lines_split[1] = lines_split[1].split(' ')
    arrays_without_empty_strings = [[x for x in arr if x != ''] for arr in lines_split]

    copies_of_current_card = dict_of_copies[index]
    index_of_copy = index + 1

    if index_of_copy not in dict_of_copies and index_of_copy < len(rows):
        dict_of_copies[index_of_copy] = 0

    for winning_card in arrays_without_empty_strings[0]:
        if index_of_copy >= len(rows):
            break
        if winning_card in arrays_without_empty_strings[1]:
            if index_of_copy not in dict_of_copies and index_of_copy < len(rows):
                dict_of_copies[index_of_copy] = 0
            dict_of_copies[index_of_copy] += copies_of_current_card
            index_of_copy += 1

total_cards = sum(dict_of_copies.values())
print(total_cards)
