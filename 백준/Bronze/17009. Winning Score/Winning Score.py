a, b = 0, 0
for i in reversed(range(1,4)):
    a = a+int(input())*i
for i in reversed(range(1,4)):
    b = b+int(input())*i
if a==b:
    print("T")
elif a>b:
    print("A")
else:
    print("B")