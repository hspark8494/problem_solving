import sys

input = sys.stdin.readline
cards = list(range(21))

for _ in range(10):
    s, e = map(int,input().rstrip().split(" "))
    while s<e:
        cards[s], cards[e] = cards[e], cards[s]
        s+=1
        e-=1

for i in range(1, 21):
    print(cards[i], end=" ")