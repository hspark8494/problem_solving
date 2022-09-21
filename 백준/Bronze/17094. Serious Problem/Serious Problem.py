input()
e=0
yee=0
for x in input():
    if x=="e":
        e=e+1
    elif x=="2":
        yee=yee+1
if e>yee:
    print("e")
elif yee>e:
    print("2")
else:
    print("yee")