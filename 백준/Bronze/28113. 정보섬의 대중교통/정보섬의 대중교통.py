N, A, B = map(int, input().split(" "))
if max(N, B) > A:
    print("Bus")
elif max(N, B) < A:
    print("Subway")
else:
    print("Anything")