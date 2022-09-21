def solution(dirs):
    moves = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }
    moved = set()
    result = 0
    pos = (0, 0)
    for s in dirs:
        m = moves[s]
        t = (m[0]+pos[0], m[1]+pos[1])
        if abs(t[0]) <= 5 and abs(t[1]) <= 5:
            if((pos, t) not in moved or (t, pos) not in moved):
                result += 1
            moved.add((pos, t))
            moved.add((t, pos))
            pos = t
    return result