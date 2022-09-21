def hanoi(n, start, dest, via, li):
    if n <= 1:
        li.append([start, dest])
        return li

    hanoi(n - 1, start, via, dest, li)
    li.append([start, dest])
    hanoi(n - 1, via, dest, start, li)

    return li

n = int(input())
if n:
    li = hanoi(n, 1, 3, 2, [])
    print(2**n-1)
    for l in li:
        print(*l)
else:
    print(0)