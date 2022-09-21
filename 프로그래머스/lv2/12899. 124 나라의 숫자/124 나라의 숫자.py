def solution(n):
    result = ""
    while n > 0:
        n -= 1
        result = result + "124"[n % 3]
        n = n//3
    return result[::-1]
