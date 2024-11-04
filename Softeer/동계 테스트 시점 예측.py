import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt():
    for i in range(n):
        for j in range(m):
            if ice[i][j] >= 3:
                ice[i][j] = 0
            elif ice[i][j] >= 2:
                ice[i][j] = 1
    return

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    visited = [[0] * m for _ in range(n)]

    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] != 1:
                if ice[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    ice[nx][ny] += 1

    melt()
    return 


def check():
    for i in range(n):
        if sum(ice[i]):
            return True

    return False
    

n, m = map(int, input().split())

q = deque()

ice = [[] for _ in range(n)]

for i in range(n):
    ice[i] = list(map(int, input().split()))

answer = 0

while check():
    bfs(0, 0)
    answer += 1

print(answer)

