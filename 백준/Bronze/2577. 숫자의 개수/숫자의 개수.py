a = str(int(input()) * int(input()) * int(input()))

l = [0] * 10

for c in a:
    l[int(c)] += 1

for i in l:
    print(i)