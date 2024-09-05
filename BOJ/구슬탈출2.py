import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline()) for _ in range(x)]

q = deque()

r_x = 0
r_y = 0
b_x = 0
b_y = 0

for i in range(x):
    for j in range(y):
        if board[i][j] == 'R':
            r_x, r_y = i, j
        if board[i][j] == 'B':
            b_x, b_y = i, j
        
q.append((r_x, r_y, b_x, b_y, 0))

visited = [(r_x, r_y, b_x, b_y)]


while q:
    rx, ry, bx, by, c = q.popleft()

    if board[rx][ry] == 'O':
        print(c)
        exit(0)
    
    if c == 10:
        continue

    for i in range(4):
        nrx, nry = rx, ry
        while True:
            nrx += dx[i]
            nry += dy[i]
            if board[nrx][nry] == '#':
                nrx -= dx[i]
                nry -= dy[i]
                break
                
            if board[nrx][nry] == 'O':
                break
        
        nbx, nby = bx, by
        while True:
            nbx += dx[i]
            nby += dy[i]
            if board[nbx][nby] == '#':
                nbx -= dx[i]
                nby -= dy[i]
                break
            if board[nbx][nby] == 'O':
                break
        
        if board[nbx][nby] == 'O':
            continue

        if nrx == nbx and nry == nby:
            if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        
        if (nrx, nry, nbx, nby) not in visited:
            visited.append((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, c+1))

print(-1)


        

                






