import sys
input = sys.stdin.readline

while True:
    li = list(map(int, input().split()))
    if li[0] == 0 and li[1] == 0 and li[2] == 0:
        break

    if(li[1] - li[0] == li[2] - li[1]):
        print("AP", li[2] + (li[1] - li[0]))
    else:
        print("GP", li[2] * (li[1] // li[0]))