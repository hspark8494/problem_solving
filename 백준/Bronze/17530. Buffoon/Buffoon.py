li =[]
for i in range(int(input())):
    li.append(int(input()))

if max(li)==li[0]:
    print("S")
else:
    print("N")