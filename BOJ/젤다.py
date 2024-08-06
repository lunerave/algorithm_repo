import heapq

idx = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    n = int(input())

    if n == 0:
        break

    distance = [[10e9]*n for _ in range(n)]

    graph = []

    q = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # min heap 사용을 통해서 가장 작은 코스트로 가는 방식을 먼저 탐색
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        c, x, y = heapq.heappop(q)

        if c > distance[n-1][n-1]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = c + graph[nx][ny]
                if distance[nx][ny] > nc:
                    distance[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

    print("Problem " + str(idx) +": " + str(distance[n-1][n-1]))
    idx += 1
    


