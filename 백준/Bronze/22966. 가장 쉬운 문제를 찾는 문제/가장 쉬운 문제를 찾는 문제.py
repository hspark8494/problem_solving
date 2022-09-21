import sys
print(sorted(list(map(lambda y: y.split(" "), sys.stdin.readlines()[1:])), key=lambda x: str(x[1]))[0][0])