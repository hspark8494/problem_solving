def solution(cards):
    visited = [False] * len(cards)
    cards = list(map(lambda x: x-1, cards))
    li = []
    for i in range(len(cards)):
        if not visited[i]:
            li.append(dfs(i, 0, cards, visited))
    li.sort(reverse=True)

    if len(li) > 1:
        return li[0] * li[1]
    else:
        return 0

def dfs(curr:int, cnt:int, cards:list, visited:list) -> int:
    visited[curr] = True
    next = cards[curr]
    if not visited[next]:
        cnt = dfs(next, cnt, cards, visited)
    return cnt+1