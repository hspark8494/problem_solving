li = [input() for x in range(int(input()))]
li[0] = list(li[0])

for k in range(len(li[0])):
    for i in range(1,len(li)):
        if li[0][k] != li[i][k]:
            li[0][k]="?"
            break

print("".join(li[0]))