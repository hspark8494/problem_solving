for m in range(3):
    s = sum(map(int, input().split()))

    print({0:"D", 1:"C", 2:"B", 3:"A", 4:"E"}.get(s))