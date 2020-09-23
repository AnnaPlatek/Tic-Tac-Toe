text = input()
#text = text.lower()
words = text.split()
for word in words:
    word_lower = word.lower()
    if word_lower.startswith('www.') or word_lower.startswith('https://') or word_lower.startswith('http://'):
        print(word)


