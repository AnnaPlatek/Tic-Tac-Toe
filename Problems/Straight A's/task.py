grades_inp = input().split()
a_num = 0
for grade in grades_inp:
    if grade == 'A':
        a_num += 1
grades_list_len = len(grades_inp)
a_ratio = a_num / grades_list_len
print(round(a_ratio, 2))