book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = dict()
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    elif word in word_counter:
        word_counter[word] = word_counter[word] + 1

word_counter2 = dict()
for word in book_title:
    word_counter2[word] = word_counter2.get(word, 0) + 1

print(word_counter)
print(word_counter2)

list_sorted = sorted(list(word_counter2))
print(list_sorted)