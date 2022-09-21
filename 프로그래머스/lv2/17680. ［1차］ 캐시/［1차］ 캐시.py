from collections import deque

def solution(cacheSize, cities):
    dq = deque()
    if cacheSize==0:
        return len(cities) * 5
    result = 0
    for city in cities:
        city = city.lower()
        if city not in dq:
            result += 5
            if len(dq) >= cacheSize:
                dq.popleft()
            dq.append(city)
        else:
            result += 1
            dq.remove(city)
            dq.append(city)
    return result
