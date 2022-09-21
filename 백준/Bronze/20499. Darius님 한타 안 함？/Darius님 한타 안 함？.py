i = list(map(int, input().split("/")))
if i[0]+i[2]<i[1] or i[1]==0:
    print("hasu")
else:
    print("gosu")