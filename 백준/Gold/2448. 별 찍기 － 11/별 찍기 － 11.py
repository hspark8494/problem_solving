def draw_star(n):
    if n==3:
        return ["  *  ", " * * ", "*****"]
    tmp = draw_star(n//2)
    result = []
    for t in tmp:
        result.append(" " * (n//2) + t + " " * (n//2))
    for t in tmp:
        result.append(t +" "+ t)
    return result

print(*draw_star(int(input())), sep="\n")