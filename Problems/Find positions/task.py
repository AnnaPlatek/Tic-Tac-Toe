num_seq = input().split()
x_value = input()
position = []
i = 0
for num in num_seq:
    if x_value == num:
        position.append(str(i))
    i += 1
position_str = ' '.join(position)
if len(position) > 0:
    print(position_str)
else:
    print('not found')
