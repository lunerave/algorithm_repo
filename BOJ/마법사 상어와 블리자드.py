N, M = list(map(int, input().split()))

board = []

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

for _ in range(N):
    board.append(list(map(int, input().split())))

order = []

for _ in range(M):
    order.append(list(map(int, input().split())))

shark_x, shark_y = N//2, N//2

def move2list(board, x, y):
    new = []
    cnt = 1
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]
    d = 0
    rotate = 0
    while True:
        for i in range(cnt):
            x = x + ddx[d]
            y = y + ddy[d]
            if x == 0 and y == -1:
                return new
            if i == cnt - 1:
                d = (d + 1) % 4
            if board[x][y] != 0:
                new.append(board[x][y])
                
        rotate += 1
        if rotate == 2:
            rotate = 0
            cnt += 1

def list2board(arr, x, y):
    cnt = 1
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]
    d = 0
    rotate = 0
    idx = 0
    while True:
        for _ in range(cnt):
            x = x + ddx[d]
            y = y + ddy[d]

            if x == 0 and y == -1:
                return

            board[x][y] = arr[idx]
            idx += 1
        
        d = (d + 1) % 4
        rotate += 1

        if rotate == 2:
            rotate = 0
            cnt += 1



answer = 0

for d, s in order:
    for i in range(1, s+1):
        nx = shark_x + dx[d]*i
        ny = shark_y + dy[d]*i

        if 0<=nx<N and 0<=ny<N:
            board[nx][ny] = 0
        
    new_arr = move2list(board, shark_x, shark_y)

    flag = 0
    while flag == 0:
        flag = 1
        temp = []
        cnt = 0
        for i in range(len(new_arr)):
            cnt += 1
            if i == len(new_arr) - 1:
                temp.append((cnt, new_arr[i]))
            elif new_arr[i+1] != new_arr[i]:
                temp.append((cnt, new_arr[i]))
                cnt = 0
        new_arr = []
        for cnt, n in temp:
            if cnt >= 4:
                flag = 0
                answer += n*cnt
            else:
                new_arr += [n] * cnt
    
    new_arr = []

    for cnt, n in temp:
        new_arr += [cnt, n]

    new_arr += [0] * (N**2 - len(new_arr))

    list2board(new_arr, shark_x, shark_y)
    
print(answer)
    

