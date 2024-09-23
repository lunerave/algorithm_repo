from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

lake = []

# 백조 위치 저장
swan = []

answer = 0

# 녹은 호수를 전체 탐색하는 것이 아니라, 이전에 녹은 위치만 탐색하면 된다.
# q, q_next: 백조의 위치 이동
# wq, wq_next: 얼음 위치 이동
q, wq, q_next, wq_next = deque(), deque(), deque(), deque()

# qv, wv 백조와 얼음 위치 경로 저장
qv = [[0]*c for _ in range(r)]
wv = [[0]*c for _ in range(r)]

for i in range(r):
    l = list(input())
    lake.append(l)
    for j in range(c):
        if l[j] == 'L':
            swan.append((i, j))
            lake[i][j] = '.'
            wq.append((i, j))
        elif l[j] == '.':
            wv[i][j] = 1
            wq.append((i, j))

q.append((swan[0][0], swan[0][1]))
qv[swan[0][0]][swan[0][1]] = 1

# 얼음이 녹는 것에 대한 알고리즘
def melt():
    while wq:
        x, y = wq.popleft()
        if lake[x][y] == 'X':
            lake[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and wv[nx][ny] == 0:
                wv[nx][ny] = 1

                # 현재 탐색 위치가 얼음이라면 다음에 녹아야함
                if lake[nx][ny] == 'X':
                    wq_next.append((nx, ny))
                else: # 물이라면 이동
                    wq.append((nx, ny))

# 백조 이동 위치에 대한 알고리즘
def bfs():
    while q:
        x, y = q.popleft()

        # 다른 백조를 찾았다면 탐색 종료
        if x == swan[1][0] and y == swan[1][1]:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and qv[nx][ny] == 0:
                qv[nx][ny] = 1

                # 물이라면 이동
                if lake[nx][ny] == '.':
                    q.append((nx, ny))
                else:   # 물이 아니라면 다음에 탐색
                    q_next.append((nx, ny))
    
    return 0
                
while True:
    melt()
    if bfs():
        print(answer)
        break

    q, wq = q_next, wq_next
    q_next, wq_next = deque(), deque()
    answer += 1


