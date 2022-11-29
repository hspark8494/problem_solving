def solution(want, number, discount):
    target, curr = 0, 0
    for i in range(len(want)):
        target += hash(want[i]) * number[i]
    for i in range(10):
        curr += hash(discount[i])
    r = int(target==curr)
    
    for i in range(10, len(discount)):
        curr = curr - hash(discount[i-10]) + hash(discount[i])
        if(target==curr):
            r+=1

    return r