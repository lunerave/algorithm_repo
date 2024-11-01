import heapq

T = int(input())

def dijk(s):
    heap = []

    heapq.heappush(heap, (0, s))

    distance = [1e9] * (n+1)
    distance[s] = 0

    while heap:
        dis, node = heapq.heappop(heap)

        if distance[node] < dis:
            continue

        for nn, nd in maps[node]:
            ndis = nd + dis

            if distance[nn] > ndis:
                distance[nn] = ndis
                heapq.heappush(heap, (ndis, nn))

    return distance

for _ in range(T):
    n, m, t = map(int, input().split())

    s, g, h = map(int, input().split())

    maps = [[] for _ in range(n+1)]

    answer = []

    for _ in range(m):
        start, end, d = map(int, input().split())
        if (start == g and end == h) or (start == h and end == g):
            g_to_h = d
        maps[start].append((end, d))
        maps[end].append((start, d))

    cands = []

    for _ in range(t):
        cands.append(int(input()))

    distFromS = dijk(s)
    distFromG = dijk(g)
    distFromH = dijk(h)
    
    for cand in cands:
        if (distFromS[cand] == distFromS[g] + g_to_h + distFromH[cand]) or (distFromS[cand] == distFromS[h] + g_to_h + distFromG[cand]):
            answer.append(cand)
        
    answer.sort()

    print(*answer)
