"""
Objective of part1 : identify the games that are possible with only 12 red cubes, 13 green cubes, and 14 blue cubes
Check the sum of cubes for each SET.
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

    # remove 'Game X : ' and newline
    line_cleaned = ' '.join(line.strip().split(' ')[2::])
    print("line cleaned: ", line_cleaned)
    lines_split_per_set = re.split('; ', line_cleaned)

    game_isValid = True
    for elem in lines_split_per_set:
        print("set -> ", elem)
        cubes_played = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        list_split = re.split(', ', elem)
        for play in list_split:
            play = play.split()
            cubes_played[play[1]] = cubes_played.get(play[1], 0) + int(play[0])

        if (cubes_played["green"] > cubes_available["green"]) or (
                (cubes_played["red"] > cubes_available["red"]) or (cubes_played["blue"] > cubes_available["blue"])):
            print("set is not valid!")
            game_isValid = False
            break

    if game_isValid:
        print("game ok")
        print("adding game id ", (count+1), " to sum that is ", sum_id_games)
        sum_id_games += (count + 1)
        print(sum_id_games)

print(sum_id_games)
f.close()
