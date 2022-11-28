def solution(order):
    answer = 0
    li = map(int, list(str(order)))
    for i in li:
        if i>0 and i%3==0:
            answer+=1
    return answer