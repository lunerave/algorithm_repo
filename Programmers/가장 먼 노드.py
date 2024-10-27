from collections import deque

def solution(n, edge):
    answer = 0
    
    temp = []
    
    max_d = -1
    
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
        
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
        
    q = deque()
    
    q.append((1, 0)) ## start node, cost 
    
    visited[1] = 1
    
    
    while q:
        node, c = q.popleft()
        max_d = max(max_d, c)
        
        for n in graph[node]:
            if visited[n] != 1:
                visited[n] = 1
                nc = c + 1
                q.append((n, nc))
                temp.append((n, nc))
            
    for t in temp:
        if t[1] == max_d:
            answer += 1
    
    return answer