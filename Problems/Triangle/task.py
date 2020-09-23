num_inp = int(input())
char_0 = '#'
char_len = 1
space_0 = ' '
space_len = 0
for num in range(1, num_inp + 1):
    char = char_0 * char_len
    char_len += 2
    space_len = num_inp - num
    space = space_0 * space_len
    row = space + char + space
    print(row)