string_inp = input().split('_')
string_list = []
for string in string_inp:
    string = string.lower()
    string = string.capitalize()
    string_list.append(string)
print(''.join(string_list))
