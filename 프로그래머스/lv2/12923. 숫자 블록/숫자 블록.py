def solution(begin, end):
    result = []
    for i in range(begin, end+1):
        t = (0 if i==1 else 1)
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= 10000000:
                t=i//j
                break
        result.append(t)
    return result