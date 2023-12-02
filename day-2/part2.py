"""
Objective of part2 : in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
My strategy:
    for each game, iterate through sets, and find if the number of each cubes is the maximum for the triplet "green, red, blue"
    get a dictionary of maxes at the end of each game.
    multiply the 3 numbers between each other and add them to the sum of powers.

"""
import re

f = open("./input.txt", "r")

sum_of_power = 0

for count, line in enumerate(f):

    # remove 'Game X : ' and newline
    line_cleaned = ' '.join(line.strip().split(' ')[2::])
    lines_split = re.split('; |, ', line_cleaned)

    set_min_cubes_required = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for elem in lines_split:

        list_split = re.split(', ', elem)
        for play in list_split:
            play = play.split()

            set_min_cubes_required[play[1]] = int(play[0]) if set_min_cubes_required.get(play[1]) < int(play[0]) \
                else set_min_cubes_required.get(play[1])

    print(lines_split)
    print(set_min_cubes_required)

    power_of_game = set_min_cubes_required["green"] * set_min_cubes_required["blue"] * set_min_cubes_required["red"]
    print("power of game : ", power_of_game)
    sum_of_power += power_of_game

print("total sum : ", sum_of_power)
f.close()
