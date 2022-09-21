from sys import stdin

input = stdin.readline

pattern = input().rstrip()
target = input().rstrip()
length = len(pattern)

codes = [0 for _ in range(26)]
acc = [0 for _ in range(26)]

for s in pattern:
    codes[ord(s)-97]+=1

try:
    for i in range(length):
        acc[ord(target[i])-97]+=1

    result = set()
    if acc==codes:
        result.add(hash(target[:length]))


    for i in range(length, len(target)):
        acc[ord(target[i-length])-97] -= 1 
        acc[ord(target[i])-97] += 1
        if acc == codes:
            result.add(hash(target[i-length+1:i+1]))
    print(len(result))
except:
    print(0)
