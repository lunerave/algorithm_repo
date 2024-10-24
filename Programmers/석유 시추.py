from collections import deque

def solution(land):
    
    
    answer = 0
    
    dp = [0] * len(land[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land[0])):
        for j in range(len(land)):
            if land[j][i] == 1 and visited[j][i] == 0:
                y_array = set()
                count = 1
                
                q = deque()
                
                q.append((j, i))
                
                visited[j][i] = 1
                
                while q:
                    x, y = q.popleft()
                    
                    y_array.add(y)
                    
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and visited[nx][ny] == 0:
                            if land[nx][ny] == 0:
                                continue
                            
                            visited[nx][ny] = 1
                            count += 1
                            q.append((nx, ny))
                            
                for y in y_array:
                    dp[y] += count
        
    
    return max(dp)