import sys
s = set()
for _ in range(int(sys.stdin.readline())):
	s.add(sys.stdin.readline().rstrip())

print('\n'.join(sorted(s, key=lambda x: (len(x),x))))