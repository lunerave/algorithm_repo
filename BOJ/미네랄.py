from collections import deque

r, c = map(int, input().split())

maps = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    maps.append(list(input()))

n = int(input())

arrows = list(map(int, input().split()))

# 왼쪽에서 미네랄을 깬다
# 해당 높이에 미네랄이 없을 경우 무시
def breakleftm(h):
    for lc in range(c):
        if maps[r-h][lc] == 'x':
            maps[r-h][lc] = '.'
            return r-h, lc
    
    return -1, -1

# 오른쪽에서 미네랄을 깬다
# 해당 높이에 미네랄이 없을 경우 무시
def breakrightm(h):
    for rc in range(c-1, -1, -1):
        if maps[r-h][rc] == 'x':
            maps[r-h][rc] = '.'
            return r-h, rc
    
    return -1, -1

# 부서진 미네랄 근처에서 BFS를 통해 연결된 클러스터 탐색
def findclusters(x, y):
    visited = [[0]*c for _ in range(r)]

    visited[x][y] = 1

    q = deque()

    q.append((x, y))

    while q:
        x, y = q.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 'x' and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
    
    return visited

# 클러스터 내에서 가장 낮은 높이 탐색
def get_min_x(visited):
    min_x_list = [-1] * c

    for y in range(c):
        for x in range(r-1, -1, -1):
            if visited[x][y]:
                min_x_list[y] = x
                break
    
    return min_x_list

# 클러스터가 얼만큼 떨어져야하는 지 탐색
def get_fall_h(min_y_list):
    min_diff = 100

    for y, min_y in enumerate(min_y_list):
        if min_y == -1:
            continue

        for x in range(min_y+1, r):
            if maps[x][y] == 'x':
                min_diff = min(min_diff, x - min_y - 1) # 처음 만난 미네랄이 5, min_y가 3이라면 1칸 내릴 수 있음
                break
            if x == r-1: # 바닥
                min_diff = min(min_diff, x - min_y) # 바닥이 5, min_y가 3이라면 2칸 내릴 수 있음
                
    return min_diff

# 클러스터 내리기
def fall(h, visited):
    for x in range(r-1, -1, -1):
        for y in range(c):
            if not visited[x][y]:
                continue
            maps[x][y] = '.'
            maps[x+h][y] = 'x'


for i in range(n):
    # 왼쪽 오른쪽 턴을 정해준다. 첫 번째는 왼쪽에서부터 시작
    if i%2==0:
        x, y = breakleftm(arrows[i])
    else:
        x, y = breakrightm(arrows[i])
    
    # 부서진 미네랄이 없으면 무시
    if x == -1 and y == -1:
        continue
    
    # 부서진 미네랄 근처의 클러스터만 탐색
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 'x':
            visited = findclusters(nx, ny)

            min_x_list = get_min_x(visited)

            # 만약 r-1이 있다면, 해당 클러스터는 땅과 닿아있다.
            if r-1 in min_x_list:
                continue

            fall_h = get_fall_h(min_x_list)
            fall(fall_h, visited)

            break

for m in maps:
    print(*m, sep= "")

