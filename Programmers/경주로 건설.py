from collections import deque


def bfs(board, dir):
    n = len(board)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    cost = [[1e8] * n for _ in range(n)]
    
    cost[0][0] = 0
    
    queue = deque()
    queue.append((0, 0, 0, dir)) ## x, y, cost, dir
    
    while queue:
        x, y, c, d = queue.popleft()
        
        if x == n-1 and y == n-1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = i
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if board[nx][ny] == 1:
                continue
            
            if nd == d:
                nc = c + 100
            else:
                nc = c + 600
                
            if nc < cost[nx][ny]:
                cost[nx][ny] = nc
                queue.append((nx, ny, nc, nd))
                
                
    return cost[-1][-1]
        


def solution(board):
    answer = min(bfs(board, 0), bfs(board, 2))
    
    return answer