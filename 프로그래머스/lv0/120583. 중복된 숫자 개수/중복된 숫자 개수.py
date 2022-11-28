def solution(array, n):
    result = 0
    for i in array:
        if i == n:
            result+=1
    return result