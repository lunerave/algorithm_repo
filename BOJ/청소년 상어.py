import copy
answer = 0

sea = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for _ in range(4):
    temp = list(map(int, input().split()))
    fish = []
    for i in range(4):
        f = [temp[i*2]] + [temp[i*2+1]-1]
        fish.append(f)
    sea.append(fish)


        
def dfs(sx, sy, score, sea):
    global answer
    score += sea[sx][sy][0]
    answer = max(answer, score)

    sea[sx][sy][0] = 0

    for f in range(1, 17):
        ix, iy = -1, -1
        for x in range(4):
            for y in range(4):
                if sea[x][y][0] == f:
                    ix, iy = x, y
                    break
        if ix == -1 and iy == -1:
            continue

        d = sea[ix][iy][1]

        for i in range(8):
            nd = (d + i) % 8
            nx = ix + dx[nd]
            ny = iy + dy[nd]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if sx == nx and sy == ny:
                    continue
                sea[ix][iy][1] = nd
                sea[ix][iy], sea[nx][ny] = sea[nx][ny], sea[ix][iy]
                break

    s_d = sea[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i

        if (0 <= nx < 4 and 0 <= ny < 4) and sea[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(sea))


dfs(0, 0, 0, sea)
print(answer) 
    



