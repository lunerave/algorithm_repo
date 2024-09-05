N, M, K = list(map(int, input().split()))

answer = 0

sea = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    sea.append(list(map(int, input().split())))

shark_move = [[] for _ in range(M)]

shark_d = list(map(int, input().split()))

shark = [[] for _ in range(M)]

for i in range(M):
    for _ in range(4):
        shark_move[i].append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if sea[i][j] != 0:
            shark[sea[i][j]-1] = [i, j, shark_d[sea[i][j]-1]-1]
        sea[i][j] = [0, 0]

def smell(sea, shark):
    for i in range(len(shark)):
        if shark[i]:
            x, y, d = shark[i]
            sea[x][y] = [K, i]
    return sea

def next(sea):
    for i in range(N):
        for j in range(N):
            if sea[i][j][0] > 0:
                sea[i][j][0] -= 1
    
    return sea

def move(shark):
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(shark)):
        if shark[i]:
            x, y, d = shark[i]
            cand = []
            my_cand = []
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    if sea[nx][ny][0] == 0:
                        cand.append((nx, ny, k))
                    elif sea[nx][ny][1] == i:
                        my_cand.append((nx, ny, k))
            nd = d
            if not cand:
                cand = my_cand
                
            if len(cand) > 1:
                for r in shark_move[i][d]:
                    flag = False
                    for a, b, c in cand:
                        if c == r-1:
                            nd = r-1
                            flag = True
                            break
                    if flag == True:
                        break
            else:
                nd = cand[0][2]
            shark[i] = [x+dx[nd], y+dy[nd], nd]
            temp[x+dx[nd]][y+dy[nd]].append(i)

    for i in range(N):
        for j in range(N):
            if len(temp[i][j]) > 1:
                temp[i][j].sort()
                for k in temp[i][j][1:]:
                    shark[k] = []
    
    cnt = 0
    for i in range(M):
        if shark[i]:
            cnt += 1
    return shark, cnt

for i in range(1000):
    sea = smell(sea, shark)
    shark, live = move(shark)
    sea = next(sea)
    if live == 1:
        print(i+1)
        exit(0)
    
print(-1) 





            




