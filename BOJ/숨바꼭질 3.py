from collections import deque

n, k = map(int, input().split())

q = deque()

q.append((n, 0))

visited = [0] * 100001

visited[n] = 1

dx = [-1, 1]

while q:
    now, cost = q.popleft()

    if now == k:
        print(cost)
        break

    nn = now * 2

    if 0 <= nn <= 100000 and visited[nn] == 0:
        q.append((nn, cost))
        visited[nn] = 1

    for i in range(2):
        nn = now + dx[i]
        nc = cost + 1

        if 0 <= nn <= 100000 and visited[nn] == 0:
            q.append((nn, nc))
            visited[nn] = 1
        

