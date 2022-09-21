from sys import stdin
input = stdin.readline

trie = {}
words = []
word_set = {}
for i in range(int(input())):
    tmp = input().rstrip()
    if not tmp in word_set:
        word_set[tmp] = 1
        words.append(tmp)
    else:
        word_set[tmp] += 1
        words.append(tmp+str(word_set[tmp]))

for word in words:
    curr = trie
    acc = ""
    flag = False
    for w in word:
        if w.isnumeric():
            print(word)
            flag = True
            break
        if w not in curr:
            curr[w] = {}
            if not flag:
                print(acc+w)
                flag = True
        curr = curr[w]
        acc += w
    if not flag:
        print(word)
