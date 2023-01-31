N = int(input())
S = input()

p = ['ABC', 'BABC','CCAABB']
name = ['Adrian','Bruno','Goran']
r = [0, 0, 0]

for i, c in enumerate(S):
    for j, word in enumerate(p):
        if(c == word[i%len(word)]):
            r[j] += 1
mx = max(r)
print(mx)
for i in range(3):
    if r[i] == mx:
        print(name[i])
