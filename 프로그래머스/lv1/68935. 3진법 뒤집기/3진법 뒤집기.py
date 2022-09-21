def solution(n):
    acc = ""
    answer = 0
    while n>=3:
        acc = acc+str(n%3)
        n = n//3
    acc += str(n)
    acc = str(int(acc))
    for i, s in enumerate(reversed(acc)):
        answer += (int(s)*(3**i))
    return answer