N, M = list(map(int, input().split()))

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

basket = []
move = []

for _ in range(N):
    basket.append(list(map(int, input().split())))

for _ in range(M):
    move.append(list(map(int, input().split())))

cloud = [(N-1, 0), (N-2, 0), (N-1, 1), (N-2, 1)]

dxy = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

for d, s in move:
    temp_cloud = []
    visited = [[0] * N for _ in range(N)]
    for x, y in cloud:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N

        basket[nx][ny] += 1

        temp_cloud.append((nx, ny))
    
    for tx, ty in temp_cloud:
        cnt = 0
        for xy in dxy:
            nx = tx + xy[0]
            ny = ty + xy[1]

            if 0 <= nx < N and 0 <= ny < N and basket[nx][ny] != 0:
                cnt += 1
        
        basket[tx][ty] += cnt
        visited[tx][ty] = 1

    cloud = []

    for i in range(N):
        for j in range(N):
            if basket[i][j] > 1 and visited[i][j] != 1:
                cloud.append((i, j))
                basket[i][j] -= 2


answer = 0

for i in range(N):
    answer += sum(basket[i])

print(answer)
    
                

    
    




