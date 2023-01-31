from collections import defaultdict
import sys
input = sys.stdin.readline

name = input().rstrip()
team_list = [input().rstrip() for _ in range(int(input()))]
team_list.sort()
result = ''
curr = -1
for team in team_list:
    d = defaultdict(int)
    for c in name+team:
        if c in "LOVE":
            d[c] += 1
    r = ((d['L']+d['O']) * (d['L']+d['V']) * (d['L']+d['E']) * (d['O']+d['V']) * (d['O']+d['E']) * (d['V']+d['E'])) % 100
    if r>curr:
        curr = r
        result = team

print(result)