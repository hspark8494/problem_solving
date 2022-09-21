li = sorted(list(map(int,input().split())))
if li[0] == li[1] and li[1]==li[2] and li[0]==li[2]:
    print(2)
elif li[0]**2 + li[1]**2 == li[2]**2:
    print(1)
else:
    print(0)