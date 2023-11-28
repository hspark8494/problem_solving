def solution(order):
    answer = 0
    for i in order:
        if i in["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            answer += 5000
        else:
            answer += 4500
    return answer