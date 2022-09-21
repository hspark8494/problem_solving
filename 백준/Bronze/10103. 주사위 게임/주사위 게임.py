s1, s2 = 100, 100

for m in range(int(input())):
    a, b = map(int, input().split())
    if a>b:
        s2 = s2-a
    elif a<b:
        s1 = s1-b
    
print(s1)
print(s2)