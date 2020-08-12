vowels = 'aeiou'
# create your list here
word = input()
new_list = [char for char in word if char in vowels]
print(new_list)