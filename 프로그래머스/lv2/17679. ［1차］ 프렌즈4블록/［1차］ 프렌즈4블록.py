def solution(m, n, board):
    board_list = []
    for i in range(n):
        li = []
        for j in range(m):
            li.append(board[j][i])
        board_list.append(li[::-1])
    result = 0

    while True:
        check = [[False for _ in range(len(b))] for b in board_list]   
        curr = 0
        
        for (i,b) in enumerate(board_list):
            for (j,e) in enumerate(b):
                solve(i,j,e,board_list,check)
        
        for (i,c) in enumerate(check):
            for j in reversed(range(len(c))):
                if check[i][j]:
                    curr+=1
                    board_list[i].pop(j)
        if curr>0:
            result+=curr
            
        else:
            return result

def solve(i,j,val,board_list,check):
    try:
        if val==board_list[i][j+1] and val==board_list[i+1][j] and val==board_list[i+1][j+1]:
            check[i][j] = True
            check[i][j+1] = True
            check[i+1][j] = True
            check[i+1][j+1] = True
    except Exception:
        pass