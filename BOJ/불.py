from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c = map(int, input().split()) 

maps = []

answer = 10e9

for _ in range(r):
    maps.append(input())

# 지훈이 위치
J = 0

# 불의 좌표로 시작하는 모든 경로를 BFS를 통해 저장
fires = deque()
# 불의 경로 저장 배열
fire = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'J':
            J = (i, j)
        
        if maps[i][j] == 'F':
            fires.append((i, j))
            fire[i][j] = 1

# 불이 이동할 때 마다 해당 위치의 시간 저장
while fires:
    fx, fy= fires.popleft()

    for i in range(4):
        nx = fx + dx[i]
        ny = fy + dy[i]

        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == '.' and fire[nx][ny] == 0:
            fire[nx][ny] = fire[fx][fy] + 1
            fires.append((nx, ny))

q = deque()

q.append((J[0], J[1]))

# 지훈이의 경로 저장
visited = [[0]*c for _ in range(r)]

visited[J[0]][J[1]] = 1

while q:
    x, y = q.popleft()

    # 모서리에 닿으면 탈출 성공
    if x == 0 or y == 0 or x == r-1 or y == c-1:
        answer = visited[x][y]
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == '.' and visited[nx][ny] == 0:
            # 해당 경로를 지날 때 불보다 빠르게 지나갔거나, 불의 경로가 아니어야 한다
            if fire[nx][ny] > visited[x][y] + 1 or fire[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

if answer == 10e9:
    print("IMPOSSIBLE")
else:
    print(answer)







