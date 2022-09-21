s = 0
for i in range(5):
    k = int(input())
    if k<40:
        k=40
    s=k+s

print(s//5)
