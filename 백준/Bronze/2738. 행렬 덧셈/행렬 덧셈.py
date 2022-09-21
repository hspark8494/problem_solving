n, m = map(int, input().split(" "))
li = []
for _ in range(n*2):
    li.append(list(map(int, input().split(" "))))
for (x,y) in zip(li[n:], li[:n]):
    for i in range(m):
        print(x[i]+y[i], end=" ")
    print()