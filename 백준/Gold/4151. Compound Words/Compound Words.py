import sys

trie = {}
lines = sys.stdin.readlines()

for line in lines:
    line = line.rstrip()
    curr = trie
    for l in line:
        if not l in curr:
            curr[l] = {}
        curr = curr[l]
    curr["end"] = {}

result = []
def search(string:str):
    tmp = trie
    for s in string:
        if s in tmp:
            tmp = tmp[s]
        else:
            return False
    return "end" in tmp

for line in lines:
    line = line.rstrip()
    curr = trie
    for idx in range(len(line)-1):
        if line[idx] in curr:
            curr=curr[line[idx]]
            if "end" in curr and search(line[idx+1:]):
                result.append(line)
                break
        else:
            break

print(*sorted(result), sep="\n")