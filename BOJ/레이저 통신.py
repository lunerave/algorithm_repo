from collections import deque
from sys import stdin
input = stdin.readline

w, h = map(int, input().split())

answer = 0

maps = []

Cs = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(h):
    line = list(input())
    maps.append(line)
    for j in range(w):
        if line[j] == 'C':
            Cs.append((i, j))
            maps[i][j] = '.'

q = deque()

# 출발
q.append((Cs[0][0], Cs[0][1]))

visited = [[10e9]*w for _ in range(h)]

visited[Cs[0][0]][Cs[0][1]] = -1

while q:
    x, y = q.popleft()

    # 도착
    if x == Cs[1][0] and y == Cs[1][1]:
        print(visited[Cs[1][0]][Cs[1][1]])
        break 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while True:
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == '.':
                # 현재 경로가 탐색 중인 위치보다 거울의 수가 적다면 탐색
                if visited[nx][ny] >= visited[x][y] + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    nx += dx[i]
                    ny += dy[i] 
                else:
                    break
            else:
                break
