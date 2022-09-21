input()
l = sorted(map(int, input().split()))
x = int(input())
s = 0
for i in l:
    if i==x:
        s+=1
print(s)
