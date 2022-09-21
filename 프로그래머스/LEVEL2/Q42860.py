# Q42860 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860#
def solution(name):
    result = 0
    size = len(name)
    moves = []

    for (i, s) in enumerate(name):
        t = ord(s) - 65
        result += t if t < 13 else 26-t
        if s != "A" and i != 0:
            moves.append(i)

    if size == 0:
        return result

    mn = min(moves[-1], abs(size - moves[0]))
    pre = moves[0]
    for l in moves[1:]:
        mn = min(mn, (max(1, pre)*2)-1 + abs(size - l))
        mn = min(mn, (max(1, abs(size - l))*2)-1 + pre)
        pre = l

    return(result + mn)
