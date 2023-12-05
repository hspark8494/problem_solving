def solution(arr):
    li = []
    for i in arr:
        li.extend([i]*i)
    return li