import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A = list(map(int, input().rstrip().split(" ")))
    result = "none"
    for i in A:
        if i==17:
            if result=="none":
                result = "zack"
            elif result=="mack":
                result = "both"
        elif i==18:
            if result=="none":
                result = "mack"
            elif result=="zack":
                result = "both"

    print(*A, sep=" ")
    print(result)
    print()