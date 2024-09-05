N, M, K = list(map(int, input().split()))

answer = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    r -= 1
    c -= 1
    board[r][c].append([m, s, d])

for k in range(K):
    temp = []
    for i in range(N):
        for j in range(N):
            while board[i][j]:
                m, s, d = board[i][j].pop()
                nx = (i + dx[d]*s) % N
                ny = (j + dy[d]*s) % N
                temp.append((nx, ny, m, s, d))
    for x, y, m, s, d in temp:
        board[x][y].append([m, s, d])
    
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                length = len(board[i][j])
                mass = 0
                speed = 0
                d_e = 0
                d_o = 0
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    mass += m
                    speed += s
                    if d % 2 == 0:
                        d_e = 1
                    else:
                        d_o = 1
                
                mass = mass // 5 
                speed = speed // length
                if mass != 0:
                    if d_e == 1 and d_o == 1:
                        temp = [[mass, speed, 1], [mass, speed, 3], [mass, speed, 5], [mass, speed, 7]]
                        board[i][j] = temp
                    else:
                        temp = [[mass, speed, 0], [mass, speed, 2], [mass, speed, 4], [mass, speed, 6]]
                        board[i][j] = temp


for i in range(N):
    for j in range(N):
        while board[i][j]:
            m, s, d = board[i][j].pop()
            answer += m

print(answer)





