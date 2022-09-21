def draw(canvas, i):
    if i<=1:
        return canvas
    li = []
    for line in canvas:
        li.append(line*3)
    for line in canvas:
        li.append(line + " " * len(line) + line)
    for line in canvas:
        li.append(line*3)
    return draw(li, i//3)

print(*draw(["*"], int(input())), sep="\n")