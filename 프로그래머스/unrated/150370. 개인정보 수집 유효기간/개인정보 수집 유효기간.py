def to_time(time: str) -> int:
    l = list(map(int, time.split(".")))
    return (l[0]*12 + l[1])*100 + l[2]


def solution(today, terms, privacies):
    d = {}
    for term in terms:
        k, v = term.split(" ")
        d[k] = int(v)
    t = to_time(today)
    result = []
    for i, curr in enumerate(privacies):
        t_day, p = curr.split(" ")
        if t >= to_time(t_day) + d[p] * 100:
            result.append(i+1)
    return result