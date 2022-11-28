def solution(dots):
    x = sorted([i[0] for i in dots])
    y = sorted([i[1] for i in dots])
    return abs(x[0] - x[3]) * abs(y[0] - y[3])