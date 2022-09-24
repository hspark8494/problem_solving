T1, V1 = map(int, input().split(" "))
T2, V2 = map(int, input().split(" "))

if T2 < 0 and V2 >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
else:
    if T1 > T2:
        print("MCHS warns! Low temperature is expected tomorrow.")
    elif V2 > V1:
        print("MCHS warns! Strong wind is expected tomorrow.")
    else:
        print("No message")