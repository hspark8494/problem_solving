import sys
input = sys.stdin.readline
x = int(input())
result = 0
for _ in range(int(input())):
    val, n = map(int, input().split(" "))
    result += (val*n)
if x==result:
    print("Yes")
else:
    print("No")