while True:
    n = int(input())
    if not n:
        break
    st = set()

    for s in input().split(","):
        d = list(map(int, s.split("-")))
        if len(d)<2:
            if d[0]<=n:
                st.add(d[0])
        else:
            if d[1]>n:
                d[1]=n

            st.update(range(d[0],d[1]+1))

    print(len(st))
