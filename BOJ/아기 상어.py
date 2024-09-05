from collections import deque

N = int(input())

answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sea = []

for _ in range(N):
    sea.append(list(map(int, input().split())))

shark = []

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark.append((i, j))

def bfs(ox, oy):
    q = deque()

    q.append((ox, oy))

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[ox][oy] = 1
    fish = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if sea[nx][ny] < sea[ox][oy] and sea[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    fish.append((visited[nx][ny] - 1, nx, ny))
                elif sea[nx][ny] == sea[ox][oy] or sea[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return sorted(fish, key = lambda x: (x[0], x[1], x[2]))
                

ox, oy = shark[0]
size = [2, 0]


while True:
    sea[ox][oy] = size[0]
    fish = deque(bfs(ox, oy))

    if not fish:
        break
    step, nx, ny = fish.popleft()
    answer += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    sea[ox][oy] = 0
    ox, oy = nx, ny

print(answer)