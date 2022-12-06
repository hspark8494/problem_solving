def solution(s:str):
    curr = ""
    cnt = 0
    result = 0
    for c in s:
        if cnt == 0:
            curr = c
            result += 1
        if curr == c:
            cnt += 1
        else:
            cnt -= 1
    return result