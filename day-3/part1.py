"""
I did not complete it today
"""

file_path = "input.txt"

with open(file_path, "r") as file:
    data = file.read()

import re

def number_is_next_to_symbol(chain_of_number, row_index, index_number, rows):
    row_length = len(rows[0])
    regex = re.compile(r"[^\w\s.]")
    start_index = index_number - len(chain_of_number) + 1
    end_index = index_number

    array_of_adjacent_symbols = []

    # check same row
    if start_index != 0:
        array_of_adjacent_symbols.append(rows[row_index][start_index - 1])
    if end_index != (row_length - 1):
        array_of_adjacent_symbols.append(rows[row_index][end_index + 1])

    # check row above
    if row_index != 0:
        for index in range(start_index, end_index + 1):
            array_of_adjacent_symbols.append(rows[row_index - 1][index])
        if start_index != 0:
            array_of_adjacent_symbols.append(rows[row_index - 1][start_index - 1])
        if end_index != (row_length - 1):
            array_of_adjacent_symbols.append(rows[row_index - 1][end_index + 1])

    # check row below
    if row_index < (len(rows) - 1):
        for index in range(start_index, end_index + 1):
            array_of_adjacent_symbols.append(rows[row_index + 1][index])
        if start_index != 0:
            array_of_adjacent_symbols.append(rows[row_index + 1][start_index - 1])
        if end_index != (row_length - 1):
            array_of_adjacent_symbols.append(rows[row_index + 1][end_index + 1])

    # check if number is at the end of a line and symbol is on the next line
    if end_index == (row_length - 1) and row_index < (len(rows) - 1):
        array_of_adjacent_symbols.append(rows[row_index + 1][end_index])

    # check if number is at the start of a line and symbol is on the previous line
    if start_index == 0 and row_index != 0:
        array_of_adjacent_symbols.append(rows[row_index - 1][start_index])

    for symbol in array_of_adjacent_symbols:
        if regex.search(symbol) is not None:
            return True

    return False



rows = data.strip().split("\n")
sum_of_numbers = 0
for i in range(len(rows)):
    row = rows[i]
    chain_of_number = ''
    for j in range(len(row)):
        carac = row[j]
        if carac.isdigit():
            # check for entire number
            chain_of_number += carac
        elif chain_of_number != '':
            # end of chain of number found. look for adjacents
            if number_is_next_to_symbol(chain_of_number, i, j - 1, rows):
                print("this one is valid :" + chain_of_number)
                print("adding it so sum ", sum_of_numbers)
                sum_of_numbers += int(chain_of_number)
                print(sum_of_numbers)
            chain_of_number = ''

print("Sum is", sum_of_numbers)
