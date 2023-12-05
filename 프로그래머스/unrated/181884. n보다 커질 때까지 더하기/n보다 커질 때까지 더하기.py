def solution(numbers, n):
    acc = 0
    for i in numbers:
        if acc>n:
            return acc
        acc += i
    return acc