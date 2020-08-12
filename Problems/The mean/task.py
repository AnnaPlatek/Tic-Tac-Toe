numbers = input()
number_list = [float(numbers) for numbers in numbers]
sum_numbers = 0
count_numbers = 0
for i in number_list:
    sum_numbers += i
    count_numbers += 1
print(sum_numbers / count_numbers)
