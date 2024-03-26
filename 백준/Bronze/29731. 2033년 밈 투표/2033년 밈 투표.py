import sys
s = set(["Never gonna give you up",
         "Never gonna let you down",
         "Never gonna run around and desert you",
         "Never gonna make you cry",
         "Never gonna say goodbye",
         "Never gonna tell a lie and hurt you",
         "Never gonna stop"])
input = sys.stdin.readline
l = [input().rstrip() for _ in range(int(input()))]
result = "No"
for i in l:
    if i not in s:
        result = "Yes"

print(result)