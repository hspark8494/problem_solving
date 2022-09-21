while True:
    s = input()
    if s=="EOI":
        break
    s = s.upper()
    print("Found" if s.find("NEMO") >-1 else "Missing")