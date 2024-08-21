import heapq

n, m, x = map(int, input().split())

answer = 0

maps = [[] for _ in range(n+1)]

# 문제의 조건인 단방향 그래프 저장
for _ in range(m):
    s, e, t = map(int, input().split())
    maps[s].append((e, t))

# 1번 마을부터 목적지까지 Dijkstra를 통해 거리 계산
# 이후 목적지부터 마을까지 Dijkstra를 통해 거리 계산
for i in range(1, n+1):
    if i == x:
        continue

    q = []

    heapq.heappush(q, (0, i))

    distance = [10e9] * (n+1)
    distance[i] = 0

    while q:
        t, c = heapq.heappop(q)

        if distance[c] < t:
            continue

        for nc, nt in maps[c]:
            if distance[nc] > t + nt:
                distance[nc] = t + nt
                heapq.heappush(q, (distance[nc], nc))

    first_t = distance[x]

    q = []

    heapq.heappush(q, (0, x))

    distance = [10e9] * (n+1)
    distance[x] = 0

    while q:
        t, c = heapq.heappop(q)

        if distance[c] < t:
            continue

        for nc, nt in maps[c]:
            if distance[nc] > t + nt:
                distance[nc] = t + nt
                heapq.heappush(q, (distance[nc], nc))

    second_t = distance[i]
    
    answer = max(answer, first_t+second_t)

print(answer)





