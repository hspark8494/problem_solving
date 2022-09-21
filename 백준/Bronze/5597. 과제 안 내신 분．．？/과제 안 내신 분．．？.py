li = [False for _ in range(30)]
for i in range(28):
    li[int(input())-1] = True
for i in range(30):
    if not li[i]:
        print(i+1, end="\n")