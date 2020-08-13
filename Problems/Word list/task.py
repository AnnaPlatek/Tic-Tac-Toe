text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
len_list = int(input())
my_list = []
for sentense in text:
        for word in sentense:
                if len(word) <= len_list:
                        my_list.append(word)
print(my_list)