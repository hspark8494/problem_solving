def solution(chicken):
    r = 0
    while chicken>=10:
        r += chicken//10
        chicken = chicken//10 + chicken%10
    return r