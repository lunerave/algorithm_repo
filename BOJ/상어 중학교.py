from collections import deque

N, M = list(map(int, input().split()))

board = []

answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    board.append(list(map(int, input().split())))

def gravity(board):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] > -1:
                r = i
                while True:
                    r += 1
                    if r < N:
                        if board[r][j] != -2:
                            r -= 1
                            break
                    else:
                        r -= 1
                        break
                board[i][j], board[r][j] = board[r][j], board[i][j]


def bfs(x, y, c):
    visited[x][y] = 1
    q = deque()
    block_area = 1
    r_block = 0
    rainbow = []
    standard = [(x, y)]
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] == c:
                    visited[nx][ny] = 1
                    block_area += 1
                    standard.append((nx, ny))
                    q.append((nx, ny))
                elif board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    block_area += 1
                    r_block += 1
                    q.append((nx, ny))
                    rainbow.append((nx, ny))
    
    for x, y in rainbow:
        visited[x][y] = 0
    
    return [block_area, r_block, standard + rainbow]

def rotate(board):
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[N-j-1][i] = board[i][j]

    return new


def remove(bls):
    for x, y in bls:
        board[x][y] = -2

while True:
    visited = [[0] * N for _ in range(N)]

    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == 0:
                now_info = bfs(i, j, board[i][j])
                if now_info[0] > 1:
                    blocks.append(now_info)
    
    blocks.sort(key= lambda x:(-x[0], -x[1], -x[2][0][0], -x[2][0][1]))

    if not blocks:
        break

    remove(blocks[0][2])
    answer += blocks[0][0]**2

    gravity(board)

    board = rotate(board)

    gravity(board)


print(answer)






    


