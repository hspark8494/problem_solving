def hanoi(n, start, dest, via, li):
    if n <= 1:
        li.append([start, dest])
        return li

    hanoi(n - 1, start, via, dest, li)
    li.append([start, dest])
    hanoi(n - 1, via, dest, start, li)

    return li

def solution(n):
    return hanoi(n, 1, 3, 2, [])