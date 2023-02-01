import sys
lines = sys.stdin.readlines()
d = {'I': 'E', 'E': 'I', 'i': 'e', 'e': 'i'}
for line in lines:
    acc = ''
    for l in line.rstrip():
        if l in d:
            acc += d[l]
        else:
            acc += l
    print(acc)