import sys
input = sys.stdin.readline

while True:
    x = int(input())
    if x == 0:
        break
    li = [input().rstrip() for _ in range(x)]
    li.sort(key=str.lower)
    
    print(li[0])