from collections import deque

n = int(input())

m = int(input())

# 이어진 경로를 저장할 임시 배열
maps = [[] for _ in range(n+1)]


# 이어진 경로 저장
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for t in range(n):
        if temp[t] == 1:
            maps[i].append(t+1)

# 여행 경로 저장
travel = list(map(int, input().split()))

for i in range(m):
    # 이미 목적지에 도착함
    if i == m-1:
        break
    
    # 각 경로 시작점
    start = travel[i]

    # 각 경로 목적지
    dest = travel[i+1]

    visited = [0] * (n+1)

    visited[start] = 1

    q = deque()

    q.append(start)

    # 경로가 있는지 확인을 위한 flag
    is_route = 0

    while q:
        city = q.popleft()

        # 목적지에 도착
        if city == dest:
            is_route = 1
            break
        
        # 이어진 경로 탐색
        for near_city in maps[city]:
            if visited[near_city] != 1:
                visited[near_city] = 1
                q.append(near_city)
    
    if is_route == 0:
        print("NO")
        exit(0)

print("YES")





