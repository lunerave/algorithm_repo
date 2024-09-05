from collections import deque

def rotate(board, board_length, l):
    length = 2**l
    new_arr = [[0] * (board_length) for _ in range(board_length)]

    for y in range(0, board_length, length):
        for x in range(0, board_length, length):
            for i in range(length):
                for j in range(length):
                    new_arr[y + j][x + length - i - 1] = board[y + i][x + j]
    
    board = new_arr

    return board

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, Q = list(map(int, input().split()))

board_length = 2**N

board = []

for _ in range(board_length):
    board.append(list(map(int, input().split())))

L = list(map(int, input().split()))

for l in L:
    board = rotate(board, board_length, l)
    
    temp = []
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] > 0:
                cnt = 0
                for t in range(4):
                    nx = i + dx[t]
                    ny = j + dy[t]

                    if 0 <= nx < board_length and 0 <= ny < board_length and board[nx][ny] > 0:
                        cnt += 1
                
                if cnt < 3:
                    temp.append((i, j))
    
    for i, j in temp:
        board[i][j] -= 1

answer1 = 0
answer2 = 0

visited = [[0] * (board_length) for _ in range(board_length)]

for i in range(board_length):
    for j in range(board_length):
        if board[i][j] > 0 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            area = 0

            while q:
                x, y = q.popleft()
                answer1 += board[x][y]
                area += 1

                for t in range(4):
                    nx = x + dx[t]
                    ny = y + dy[t]

                    if 0<=nx<board_length and 0<=ny<board_length and board[nx][ny] >0 and visited[nx][ny]==0 :
                        visited[nx][ny] =1 
                        q.append([nx,ny])


            answer2 = max(answer2, area)


print(answer1)
print(answer2)












