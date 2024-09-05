from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def makeWall(num):
    if num == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(num+1)
                board[i][j] = 0

def bfs():
    global answer
    cnt = 0
    q = deque()

    temp_board = copy.deepcopy(board)

    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 2:
                q.append((i, j))

    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if temp_board[nx][ny] == 0:
                temp_board[nx][ny] = 2
                q.append((nx, ny))
    

    for i in range(n):
        cnt += temp_board[i].count(0)
    
    answer = max(answer, cnt)

global answer

answer = 0

n, m = list(map(int, input().split()))

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

makeWall(0)

print(answer)



            
