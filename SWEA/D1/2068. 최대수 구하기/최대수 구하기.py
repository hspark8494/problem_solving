T = int(input())

for t in range(T):
    print(f"#{t+1} {max(map(int, input().split(' ')))}")
