from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(input())

q = deque()

# 벽을 부쉈을 때 경로와 안 부쉈을 때 경로를 분리
visited = [[[0]*m for _ in range(n)] for _ in range(2)]

q.append((0, 0, 1, 1))

visited[0][0][0] = 1

answer = 10e9

while q:
    x, y, hammer, d = q.popleft()

    if x == n-1 and y == m-1:
        answer = min(answer, d)
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 부술 수 있는 횟수가 남아있을 때 -> 벽을 만나면 부수고, 이제부터 벽을 부쉈을 때를 탐색
            if hammer == 1:
                if visited[0][nx][ny] == 0:
                    if maps[nx][ny] == '1':
                        visited[1][nx][ny] = 1
                        nd = d + 1
                        q.append((nx, ny, 0, nd))
                    else:
                        visited[0][nx][ny] = 1
                        nd = d + 1
                        q.append((nx, ny, 1, nd))
            # 부술 수 있는 횟수가 없을 때 -> 벽을 만나면 진행 불가
            else:
                if visited[1][nx][ny] == 0:
                    if maps[nx][ny] == '0':
                        visited[1][nx][ny] = 1
                        nd = d + 1
                        q.append((nx, ny ,0, nd))


if answer == 10e9:
    print(-1)
else:
    print(answer)





