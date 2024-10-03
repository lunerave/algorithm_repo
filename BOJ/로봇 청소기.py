from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 위치에서 다음 위치까지의 거리 계산
def find_dist(x, y, w, h, d_x, d_y, room):
    q = deque()

    q.append((x, y, 0))

    visited = [[0]*w for _ in range(h)]

    while q:
        x, y, c = q.popleft()

        if x == d_x and y == d_y:
            return c

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and room[nx][ny] != 'x':
                nc = c + 1
                visited[nx][ny] = 1
                q.append((nx, ny, nc))

    return -1

# 더러운 칸간의 거리를 계산해서 저장해가며 가장 짧은 거리 계산
def dfs(node, cost, depth, maps, visited):
    global answer
    visited[node] = 1

    # 모든 더러운 칸 청소 완료
    if depth == len(maps)-1:
        answer = min(answer, cost)
        return
    
    for i in range(len(maps)):
        if visited[i] == 0:
            dfs(i, cost+maps[node][i], depth+1, maps, visited)
            visited[i] = 0


while True:
    w, h = map(int, input().split())

    answer = 2**31

    if w == 0 and h == 0:
        break

    dirty = []

    room = []

    for i in range(h):
        line = list(input())
        room.append(line)
        for j in range(w):
            if line[j] == '*':
                dirty.append((i, j))
                room[i][j] = '.'
            if line[j] == 'o':
                robot = (i, j)

    # 로봇에서 각 더러운 칸까지 거리 계산
    robot_to_dirty = [0]*len(dirty)

    for i, dir in enumerate(dirty):
        robot_to_dirty[i] = find_dist(robot[0], robot[1], w, h, dir[0], dir[1], room)

    # 로봇이 닿을 수 없는 칸이 있다면 -1 리턴
    if -1 in robot_to_dirty:
        print(-1)
        continue
    
    # 더러운 칸간의 거리 저장
    dirty_to_dirty = [[0]*len(dirty) for _ in range(len(dirty))]

    # 더러운 칸 간의 거리 계산
    for i in range(len(dirty)):
        for j in range(len(dirty)):
            if i == j:
                continue
            if dirty_to_dirty[i][j] != 0:
                continue
            dist = find_dist(dirty[i][0], dirty[i][1], w, h, dirty[j][0], dirty[j][1], room)
            dirty_to_dirty[i][j] = dist
            dirty_to_dirty[j][i] = dist
    
    # 로봇에서 각 더러운 칸으로 이동 후
    # 더러운 칸 간의 거리 계산 후 최소 거리 계산
    for i in range(len(dirty)):
        visited = [0] * len(dirty)
        dfs(i, robot_to_dirty[i], 0, dirty_to_dirty, visited)
    
    print(answer)
    
    

   
    

            

        
    
