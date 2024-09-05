import heapq

n, m = map(int, input().split())

maps = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())

    maps[s].append((e, c))
    maps[e].append((s, c))

heap = []

distances = [10e9] * (n+1)

distances[1] = 0

heapq.heappush(heap, (0, 1))

while heap:
    cost, node = heapq.heappop(heap)

    if cost > distances[node]:
        continue

    for an, ac in maps[node]:
        nc = cost + ac
        
        if distances[an] > nc:
            distances[an] = nc
            heapq.heappush(heap, (nc, an))

print(distances[n])




    