dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words_inp = input().split()
ok_len = 0
for word in words_inp:
    if word in dictionary:
        ok_len += 1
    else:
        print(word)
    if ok_len == len(words_inp):
        print("OK")