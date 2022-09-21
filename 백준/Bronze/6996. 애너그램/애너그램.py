import sys

input = sys.stdin.readline

N = int(input())

def counting(line:str):
    li = [0] * 26
    for s in line:
        li[ord(s)-97]+=1
    return li

for _ in range(N):
    p, q = input().rstrip().split(" ")
    if counting(p) == counting(q):
        print(f"{p} & {q} are anagrams.")
    else:
        print(f"{p} & {q} are NOT anagrams.")