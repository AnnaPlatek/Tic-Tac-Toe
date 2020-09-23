words_inp = input().split()
words_list = []
for word in words_inp:
    word = word.capitalize()
    words_list.append(word)
words_list[0] = words_list[0].lower()
print(''.join(words_list))