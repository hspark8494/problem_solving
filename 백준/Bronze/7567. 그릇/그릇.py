s = input()
cnt = 5
k = s[0]

for i in s:
    if i==k:
        cnt=cnt+5
    else:
        cnt=cnt+10
    k=i

print(cnt)