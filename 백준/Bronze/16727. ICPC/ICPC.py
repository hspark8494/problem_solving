p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

if p1+p2==s1+s2:
    if p1==s2 and s1==p2:
        print("Penalty")
    else:
        print("Persepolis" if p1<s2 else "Esteghlal")

else:
    print("Persepolis" if p1+p2>s1+s2 else "Esteghlal")
