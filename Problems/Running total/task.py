number = input()
my_sum = 0
my_sum_list = []
for char in number:
    my_sum += int(char)
    my_sum_list.append(my_sum)
print(my_sum_list)