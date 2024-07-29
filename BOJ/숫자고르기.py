n = int(input())

# 노드간의 경로 저장
graph = [[] for _ in range(n+1)]
# 문제 조건을 만족하는 노드 저장
result = []

def dfs(v, i):
    visited[v] = 1

    # 인접 노드 탐색
    for node in graph[v]:
        if not visited[node]:
            dfs(node, i)
            continue
        
        # 탐색 중 타겟 노드 발견 => 이어져 있음
        if node == i:
            result.append(node)
        

for i in range(1, n+1):
    node = int(input())
    graph[node].append(i)

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)

print(len(result))

# 작은 수부터 가능 여부 판단하므로 sort 필요 없음
# result.sort()

for num in result:
    print(num)



