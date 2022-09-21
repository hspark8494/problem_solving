def check(place):
    pos = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                pos.append((i,j))
                
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            dist = (pos[i][0]-pos[j][0], pos[i][1]-pos[j][1])
            abs_dist = (abs(dist[0]), abs(dist[1]))
            m_dist = abs_dist[0]+abs_dist[1]
            if m_dist > 2:
                continue
            elif m_dist == 2:
                if abs_dist[0] == 1 and abs_dist[1] == 1:
                    if place[pos[i][0]-dist[0]][pos[i][1]] == "O" or place[pos[i][0]][pos[i][1]-dist[1]] == "O":
                        return False
                else:
                    if place[pos[i][0]-dist[0]//2][pos[i][1]-dist[1]//2] == "O":
                        return False
            else:
                return False
    return True

def solution(places):
    result = [int(check(place)) for place in places]
    print(result)
    return result