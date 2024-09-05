from collections import deque
import heapq

def ntet(x, y):
    global answer
    temp_u = board[x][y]
    temp_d = board[x][y]
    temp_r = board[x][y]
    temp_l = board[x][y]
    temp_s = board[x][y]

    if x - 1 >= 0 and y + 1 < M and x + 1 < N:
        temp_r += board[x-1][y] + board[x][y+1] + board[x+1][y]
    if x - 1 >= 0 and x + 1 < N and y - 1 >= 0:
        temp_l += board[x-1][y] + board[x+1][y] + board[x][y-1]
    if x - 1 >= 0 and y + 1 < M and y - 1 >= 0:
        temp_u += board[x-1][y] + board[x][y+1] + board[x][y-1]
    if x + 1 < N and y + 1 < M and y - 1 >= 0:
        temp_d += board[x+1][y] + board[x][y+1] + board[x][y-1]
    if x + 1 < N and y + 1 < M:
        temp_s += board[x+1][y] + board[x][y+1] + board[x+1][y+1]
    answer = max(answer, temp_d, temp_l, temp_r, temp_u, temp_s)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = list(map(int, input().split()))


global answer

answer = 0

board = []

board_max = 0

for i in range(N):
    board.append(list(map(int, input().split())))
    board_max = max(board_max, max(board[i]))


for i in range(N):
    for j in range(M):
        ntet(i, j)
        q = []
        heapq.heappush(q, (-board[i][j], i, j, 0))
        visited = []
        visited.append((i, j))

        while q:
            s, x, y, c = heapq.heappop(q)

            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]

                if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                    ns = s - board[nx][ny]
                    nc = c + 1

                    if nc == 3:
                        answer = max(answer, -ns)
                        continue
                        
                    if -ns + board_max*(3-nc) < answer:
                        continue

                    visited.append((nx, ny))
                    heapq.heappush(q, (ns, nx, ny, nc))

print(answer)         




        
    



