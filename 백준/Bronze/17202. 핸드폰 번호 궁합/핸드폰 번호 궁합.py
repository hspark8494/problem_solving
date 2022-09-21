S1, S2 = input(), input()
comp = []

for i in range(len(S1)):
    comp.append(int(S1[i]))
    comp.append(int(S2[i]))

while len(comp) > 2:
    next = []
    for i in range(1,len(comp)):
        next.append((comp[i-1] + comp[i])%10)
    comp = next
print(str(comp[0]) + str(comp[1]))