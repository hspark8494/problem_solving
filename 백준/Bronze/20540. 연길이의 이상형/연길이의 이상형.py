x = input()
l = []
l.append("I" if x[0] == "E" else "E")
l.append("N" if x[1] == "S" else "S")
l.append("F" if x[2] == "T" else "T")
l.append("P" if x[3] == "J" else "J")

print("".join(l))