"""
This is my first take on puzzle 1, but i did not get the algorithm right:
 i thought i had to add up the cubes on each game to check if they are superior to cubes available, and not add up each set

"""
import re

f = open("./input.txt", "r")

cubes_available = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_id_games = 0

for count, line in enumerate(f):
    cubes_played = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    # remove 'Game X : ' and newline
    line_cleaned = ' '.join(line.strip().split(' ')[2::])
    print(line_cleaned)
    lines_split = re.split('; |, ', line_cleaned)

    for elem in lines_split:
        elem = elem.split()
        cubes_played[elem[1]] = cubes_played.get(elem[1], 0) + int(elem[0])

    print(lines_split)
    print(cubes_played)

    game_isValid = True
    for key in cubes_available:
        if cubes_played[key] > cubes_available[key]:
            game_isValid = False
            break

    if game_isValid:
        print("game possible")
        sum_id_games += (count+1)
    else:
        print("nonono")

print(sum_id_games)
f.close()
