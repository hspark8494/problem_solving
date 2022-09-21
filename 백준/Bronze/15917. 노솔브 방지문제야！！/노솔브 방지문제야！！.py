import sys
for _ in range(int(input())):
    s = format(int(sys.stdin.readline().rstrip()), 'b')
    print(0 if "1" in s[1:][::-1] else 1)