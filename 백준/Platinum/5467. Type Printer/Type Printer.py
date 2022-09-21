class trie:
    def __init__(self, parent):
        self.data = {}
        self.parent = parent
        self.ln = 0
        self.end = False

from sys import stdin
input = stdin.readline
words = []

tries = trie(None)
n = int(input())
for _ in range(n):
    word = input().rstrip()
    words.append(word)
    curr = tries
    ln = len(word)
    for w in word:
        if not w in curr.data:
            curr.data[w] = trie(curr)
        curr = curr.data[w]
        curr.ln = max(ln, curr.ln)
    else:
        curr.end = True


def dfs_trie(curr:trie, result):
    global n
    if curr.end:
        result.append("P")
        n -= 1
    for c in sorted(curr.data.keys(), key=lambda x: curr.data[x].ln):
        result.append(c)
        dfs_trie(curr.data[c], result)
    if n>0:
        result.append("-")
result = []
dfs_trie(tries, result)

print(len(result))
print(*result, sep="\n")