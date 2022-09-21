li = list(map(int,list(input())))
if len(li)==2:
    print(sum(li))
elif len(li)==4:
    print(20)
else:
    print(10+li[2] if li[1]==0 else li[0]+10)