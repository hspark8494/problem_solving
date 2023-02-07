def solution(k: int, m: int, score: list):
    score.sort()
    score = score[len(score)%m:]
    r = 0
    for i in range(0 ,len(score), m):
        r += score[i] * m

    return r