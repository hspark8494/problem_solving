def draw_star(n, canvas):
    if n <= 1:
        return canvas
    li = []
    ln = len(canvas)
    li.append((ln+4) * "*")
    li.append("*" +( " " * (ln+2)) +"*")
    for line in canvas:
         li.append("* " + line + " *")
    li.append("*" +( " " * (ln+2)) +"*")
    li.append((ln+4) * "*")
    return draw_star(n-1, li)

print(*draw_star(int(input()),["*"]), sep="\n")