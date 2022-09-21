def solution(name):
    result = 0
    moves = []

    for (i, s) in enumerate(name):
        t = ord(s) - 65
        result += t if t < 13 else 26-t
        if s != "A" and i != 0:
            moves.append(i)

    if len(moves) == 0:
        return result

    mn = min(moves[-1], abs(len(name) - moves[0]))
    pre = moves[0]
    for l in moves[1:]:
        mn = min(mn, pre*2 + abs(len(name) - l))
        mn = min(mn, abs(len(name) - l)*2 + pre)
        pre = l

    return(result + mn)
