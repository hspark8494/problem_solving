import sys
input = sys.stdin.readline


def check(source: list, target: list) -> bool:
    for i in range(len(source)):
        for j in range(len(source[0])):
            if source[i][j] == '#' and target[i][j] == '.':
                return False
    return True


d = {}

d[0] = ["###", "#.#", "#.#", "#.#", "###"]
d[1] = ["..#", "..#", "..#", "..#", "..#"]
d[2] = ["###", "..#", "###", "#..", "###"]
d[3] = ["###", "..#", "###", "..#", "###"]
d[4] = ["#.#", "#.#", "###", "..#", "..#"]
d[5] = ["###", "#..", "###", "..#", "###"]
d[6] = ["###", "#..", "###", "#.#", "###"]
d[7] = ["###", "..#", "..#", "..#", "..#"]
d[8] = ["###", "#.#", "###", "#.#", "###"]
d[9] = ["###", "#.#", "###", "..#", "###"]

N = int(input())
lines, T, result_list = [], [], []

for _ in range(5):
    lines.append(input().rstrip())

for i in range(N):
    li = []
    for line in lines:
        li.append(line[i*4:i*4+3])
    T.append(li)

for t in T:
    r = []
    for i, og in d.items():
        if (check(t, og)):
            r.append(i)
    if not r:
        print(-1)
        sys.exit()
    result_list.append(r)

result = 0

for i, x in enumerate(reversed(result_list)):
    result += ((10 ** i * sum(x)) / len(x))

print(result)
