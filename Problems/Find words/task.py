words_list = input().split()
s_list = []
for word in words_list:
    if word.endswith('s'):
        s_list.append(word)
print("_".join(s_list))
