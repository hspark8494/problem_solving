import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input().rstrip())
        trie = {}
        lines = []
        for _ in range(n):
            line = input().rstrip()
            lines.append(line)
            curr = trie
            for (i,c) in enumerate(line):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
                if i+1 == len(line):
                    curr["end"] = None
        result = 0
        for line in lines:
            curr = trie
            for c in line:
                if curr==trie or len(curr) > 1:
                    result += 1
                curr = curr[c]
        print(f'{round(result / n,2):.2f}' )
    except:
        break