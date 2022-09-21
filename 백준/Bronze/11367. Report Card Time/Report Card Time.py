for _ in range(int(input())):
    n,i = input().split()
    r = ""
    i = int(i)

    if i>=97:
        r = "A+"
    elif i>=90:
        r = "A"
    elif i>=87:
        r = "B+"
    elif i>=80:
        r = "B"
    elif i>=77:
        r = "C+"
    elif i>=70:
        r = "C"
    elif i>=67:
        r = "D+"
    elif i>=60:
        r = "D"
    else:
        r = "F"
    print(n,r)