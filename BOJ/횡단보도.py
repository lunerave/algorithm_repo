import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maps = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    maps[s].append((e, i))
    maps[e].append((s, i))

heap = []

# 최단 거리를 찾기 위한 min heap
# 다익스트라 사용
heapq.heappush(heap, (0, 1))

distance = [sys.maxsize] * (n+1)
distance[1] = 0

while heap:
    t, now = heapq.heappop(heap)

    if now == n:
        print(t)
        break
    # 현재 저장된 최소 시간보다 탐색 중인 경로의 시간이 더 길다면 탐색 필요 없음
    if distance[now] < t:
        continue

    for near, i in maps[now]:
        # 주기가 0이 아닐 경우 +1을 해주어야 한다
        if (t-i)%m == 0:
            nt = i+((t-i)//m)*m
        else:
            nt = i+((t-i)//m+1)*m

        # 횡단보도를 건너는데 필요한 시간 1
        if distance[near] > nt+1:
            distance[near] = nt+1
            heapq.heappush(heap, (nt+1, near))

    

