def askForInput():
    valid_values = ['X', 'O', '_']
    cells_values = input('Enter cells: ')
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

