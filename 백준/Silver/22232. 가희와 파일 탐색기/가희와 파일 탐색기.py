import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
names = [input().rstrip() for _ in range(N)]
exts = set([input().rstrip() for _ in range(M)])

def compare(filename:str):
    name, ext = filename.split(".")
    return (name, -int(ext in exts), ext)
names.sort(key=compare)

print(*names, sep="\n")