from collections import deque
import math

n, l, r = map(int, input().split())

graph = []

# 지속적으로 인구 이동이 일어날 국가 맵
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

while True:
    # 인구 이동을 나타낼 임시 배열
    people_move = [[[] for _ in range(n)] for _ in range(n)]

    # 인구 이동이 일어났는지 체크하는 flag
    people_moved = 0

    for i in range(n):
        for j in range(n):
            if j != n-1 and l <=abs(graph[i][j] - graph[i][j+1]) <= r:
                people_move[i][j].append((i, j+1))
                people_move[i][j+1].append((i, j))
                people_moved = 1
            
            if i != n-1 and l <=abs(graph[i][j]- graph[i+1][j]) <= r:
                people_move[i][j].append((i+1, j))
                people_move[i+1][j].append((i, j))
                people_moved = 1
    
    if people_moved == 0:
        break
            
    visited = [[0] * n for _ in range(n)]

    # 방문한 적이 없는 국가 탐색, bfs를 통해 방문 가능 국가의 인구 수 더하기
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                q = deque()
                cost = graph[i][j]
                q.append((i, j))
                visit = [(i, j)]

                while q:
                    cx, cy = q.popleft()

                    for x, y in people_move[cx][cy]:
                        if visited[x][y] == 0:
                            visited[x][y] = 1
                            cost += graph[x][y]
                            q.append((x, y))
                            visit.append((x, y))

                new_cost = math.floor(cost / len(visit))
                
                # 새로운 국가 맵 갱신
                for vx, vy in visit:
                    graph[vx][vy] = new_cost


    answer += 1

print(answer)
            



            



