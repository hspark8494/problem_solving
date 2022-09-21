import sys
input = sys.stdin.readline

C,N = map(int, input().split(" "))

colors = set()
names = {}

for _ in range(C):
    colors.add(input().rstrip())

for _ in range(N):
    name = input().rstrip()
    curr = names
    for n in reversed(name):
        if not n in curr:
            curr[n] = {}
        curr = curr[n]
    curr["0"] = {}

def search_names(trie:dict, query:str, ln):
    dept = 0
    curr = trie
    for i, s in enumerate(query):
        if s not in curr:
            return False
        curr = curr[s]
        dept+=1
        if "0" in curr:
            tmp = query[:i:-1]
            if tmp in colors :
                if dept + len(tmp) == ln:
                    return True
    return False

r = []
Q = int(input())
for _ in range(Q):
    query = input().rstrip()
    result = search_names(names, query[::-1], len(query))
    if result:
        r.append("Yes")
    else:
        r.append("No")

print("\n".join(r))
