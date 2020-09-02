import math
# create board
cells_values = input('Enter cells: ')
def askForInput():
    valid_values = ['X', 'O', '_']

    if len(cells_values) != 9:
        print("invalid value!")
        askForInput()
    else:
        for char in cells_values:
            if char not in valid_values:
                print("invalid value!")
                askForInput()
            else:
                continue
        print('---------')
        print('|', cells_values[0], cells_values[1], cells_values[2], '|')
        print('|', cells_values[3], cells_values[4], cells_values[5], '|')
        print('|', cells_values[6], cells_values[7], cells_values[8], '|')
        print('---------')

# *************************************************
askForInput()


# check number of valid values
x_number = 0
o_number = 0
none_number = 0
for char in cells_values:
    if char == "X":
        x_number += 1
    elif char == 'O':
        o_number += 1
    elif char == "_":
        none_number += 1

# rows victory
win1 = [cells_values[0], cells_values[1], cells_values[2]]
win2 = [cells_values[3], cells_values[4], cells_values[5]]
win3 = [cells_values[6], cells_values[7], cells_values[8]]

# column victory
win4 = [cells_values[0], cells_values[3], cells_values[6]]
win5 = [cells_values[1], cells_values[4], cells_values[7]]
win6 = [cells_values[2], cells_values[5], cells_values[8]]

# diagonal victory
win7 = [cells_values[0], cells_values[4], cells_values[8]]
win8 = [cells_values[2], cells_values[4], cells_values[6]]

victory_variants = [win1, win2, win3, win4, win5, win6, win7, win8]

x_victory = ['X','X','X']
o_victory = ['O','O','O']

# check variant impossible
if math.fabs(x_number - o_number) > 1 or ((x_victory in victory_variants) and (o_victory in victory_variants)):
    print("Impossible")

# check draw
elif none_number == 0 and x_victory not in victory_variants and o_victory not in victory_variants:
    print("Draw")

# game not finished
elif none_number > 0 and x_victory not in victory_variants and o_victory not in victory_variants:
    print("Game not finished")

# X wins
elif x_victory in victory_variants and o_victory not in victory_variants:
    print("X wins")

# O wins
elif x_victory not in victory_variants and o_victory in victory_variants:
    print("O wins")