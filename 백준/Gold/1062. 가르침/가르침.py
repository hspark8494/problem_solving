import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
d = set(['i', 'c', 't', 'n', 'a'])
s = set(['i', 'c', 't', 'n', 'a'])

sets = []

for _ in range(N):
    w = input().rstrip()
    ts = set(list(w[4:-4]))
    sets.append(ts)
    s.update(ts)

if M < 5:
    print(0)
    sys.exit()

if M > len(s):
    print(N)
    sys.exit()

s.remove('i')
s.remove('c')
s.remove('t')
s.remove('n')
s.remove('a')


mx = 0

for c in itertools.combinations(s, M-5):
    t = set(c)
    t.update(d)
    x = 0
    for n in sets:
        x += int(t.issuperset(n))
    mx = max(x, mx)

print(mx)
