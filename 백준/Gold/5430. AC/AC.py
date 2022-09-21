from collections import deque
import sys
input = sys.stdin.readline
def solve():
    reverse_called = 0
    op = input()
    n = int(input())
    li = deque()
    if n>0:
        li.extend((input().rstrip()[1:-1:]).split(","))
    else:
        input()
    for o in op:
        if o == "R":
            reverse_called+=1
        if o == "D":
            if not li:
                print("error")
                return
            if reverse_called%2 == 0:
                li.popleft()
            else:
                li.pop()
    if reverse_called%2 > 0:
        li.reverse()
    print(f"[{','.join(list(li))}]")

x = int(input())
for _ in range(x):
    solve()
