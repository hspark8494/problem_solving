li = [int(input()) for i in range(3)]

if li[0]==60 and li[1] == 60 and li[2] == 60:
    print("Equilateral")
elif sum(li) == 180 and (li[0]==li[1] or li[1]==li[2] or li[0]==li[2]):
    print("Isosceles")
elif sum(li)!=180:
    print("Error")
else:
    print("Scalene")