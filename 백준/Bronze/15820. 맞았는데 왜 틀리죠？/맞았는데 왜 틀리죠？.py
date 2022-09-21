import sys
input = sys.stdin.readline
T, S = map(int, input().split(" "))

for _ in range(T):
    case = input().rstrip().split(" ")
    if not case[0] == case[1]:
        print("Wrong Answer")
        break
else:
    for _ in range(S):
        case = input().rstrip().split(" ")
        if not case[0] == case[1]:
            print("Why Wrong!!!")
            break
    else:
        print("Accepted")