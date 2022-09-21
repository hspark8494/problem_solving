i = input()
if i.startswith("0x"):
    print(int(i,16))
elif i[0]=="0":
    print(int(i,8))
else:
    print(int(i))