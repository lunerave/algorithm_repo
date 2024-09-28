from collections import deque

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs를 통해 각 위치까지 열어야 하는 최소 문의 갯수 저장
def bfs(x, y, h, w, maps):
    q = deque()
    q.append((x, y))

    distance = [[-1]*(w+2) for _ in range(h+2)]

    distance[x][y] = 0

    while q:
        x, y = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h+2 and 0 <= ny < w+2 and maps[nx][ny] != "*" and distance[nx][ny] == -1:
                if maps[nx][ny] == '#':
                    distance[nx][ny] = distance[x][y] + 1
                    q.appendleft((nx, ny))
                else:
                    distance[nx][ny] = distance[x][y]
                    q.append((nx, ny))
    
    return distance

for _ in range(t):
    h, w = map(int, input().split())

    maps = []

    start = []

    # 상근이의 위치를 지정하기 위해서 maps 외곽에 통로 추가
    maps = [["." for _ in range(w+2)]]
    for i in range(h):
        line = list(input())
        line = ["."] + line + ["."]
        maps.append(line)
        for j in range(w+2):
            if line[j] == '$':
                start.append((i+1, j))
    maps.append(["." for _ in range(w+2)])

    # 첫 번째 죄수의 위치로부터 maps 각 위치까지 문 여는 갯수
    dist1 = bfs(start[0][0], start[0][1], h, w, maps)
    # 두 번째 죄수의 위치로부터 maps 각 위치까지 문 여는 갯수
    dist2 = bfs(start[1][0], start[1][1], h, w, maps)
    # 상근이의 위치로부터 maps 각 위치까지 문 여는 갯수
    sangeun = bfs(0, 0, h, w, maps)

    result = 10e9

    for x in range(h+2):
        for y in range(w+2):
            # 각 위치까지 세 갯수를 더하면 다 함께 문 열고 탈옥하는 것이 된다
            temp = dist1[x][y] + dist2[x][y] + sangeun[x][y]

            # 만나는 위치가 문이라면 겹치므로 2번 문 연 횟수를 빼줘야함
            if maps[x][y] == '#':
                temp -= 2

            if temp >= 0:
                result = min(result, temp)
    
    print(result)
    
    
    
    