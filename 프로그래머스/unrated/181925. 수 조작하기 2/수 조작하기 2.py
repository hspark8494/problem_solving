def solution(numLog):
    x = dict(zip([1,-1,10,-10], 'wsda'))
    log = []
    curr = numLog[0]
    for i in numLog[1:]:
        log.append(x[i-curr])
        curr = i
    return "".join(log)