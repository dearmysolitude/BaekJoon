inN = int(input())
letters=[]
for i in range(inN):
    letters.append(input())
temp = list(set(letters))

sortedW= []
for i in temp:
    sortedW.append((len(i), i))

result = sorted(sortedW)
for len_word, word in result:
    print(word)