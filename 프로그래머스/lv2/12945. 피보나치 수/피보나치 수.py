def solution(n):
    result = 0
    a = 0
    b = 1

    for i in range(1, n):
        result = a + b
        a = b
        b = result

    return result%1234567