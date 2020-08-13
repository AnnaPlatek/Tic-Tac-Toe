number = input()
my_list = [int(digit) for digit in number]
second_list = []
for n in range(len(my_list) - 1):
    mean_value = (my_list[n] + my_list[n + 1]) / 2
    second_list.append(mean_value)
print(second_list)
