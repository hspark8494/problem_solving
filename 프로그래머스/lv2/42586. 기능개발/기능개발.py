from math import ceil
def solution(progresses:list, speeds):
    li = [[x,y] for (x,y) in zip(progresses, speeds)]
    li.reverse()
    result = []
    while li:
        if(li[-1][0] < 100):
            for i in li:
                i[0] += i[1]
        else:
            t = 0
            while li:
                if li[-1][0] >= 100: 
                    li.pop()
                    t += 1
                else: break
            result.append(t)
    return result