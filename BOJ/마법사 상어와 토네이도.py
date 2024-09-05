N = int(input())

answer = 0

board = []

wind_direction = [[(-1, 0, 1), (1, 0, 1), (-2, -1, 2), (2, -1, 2), 
        (-1, -1, 7), (1, -1, 7), (-1, -2, 10), (1, -2, 10), (0, -3, 5)]
, [(0, -1, 1), (0, 1, 1), (1, -2, 2), (1, 2, 2), 
        (1, -1, 7), (1, 1, 7), (2, -1, 10), (2, 1, 10), (3, 0, 5)]
, [(-1, 0, 1), (1, 0, 1), (-2, 1, 2), (2, 1, 2), (-1, 1, 7), 
         (1, 1, 7), (-1, 2, 10), (1, 2, 10), (0, 3, 5)]
, [(0, -1, 1), (0, 1, 1), (-1, -2, 2), (-1, 2, 2), 
      (-1, -1, 7), (-1, 1, 7), (-2, -1, 10), (-2, 1, 10), (-3, 0, 5)]
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for _ in range(N):
    board.append(list(map(int, input().split())))

def storm(x, y, d):
    global answer
    sand = board[x+dx[d]][y+dy[d]]
    sand_list = [0 for _ in range(11)]
    sand_list[1] = sand // 100
    sand_list[2] = int(sand * 0.02)
    sand_list[5] = int(sand * 0.05)
    sand_list[7] = int(sand * 0.07)
    sand_list[10] = int(sand * 0.1)

    spreads = 0
    
    for i, j, p in wind_direction[d]:
        nx = x + i
        ny = y + j
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += sand_list[p]
        else:
            answer += sand_list[p]
        spreads += sand_list[p]

    board[x+dx[d]][y+dy[d]] = 0
    if 0 <= x+(dx[d]*2) < N and 0 <= y+(dy[d]*2) < N:
        board[x+(dx[d]*2)][y+(dy[d]*2)] += sand - spreads
    else:
        answer += sand - spreads

now = [N//2, N//2]
d = 0
cnt = 1 
rotate = 0
while now[0] >= 0 and now[1] >= 0:
    if rotate == 2:
        rotate = 0
        cnt += 1
    for i in range(cnt):
        storm(now[0], now[1], d)
        now[0] = now[0] + dx[d]
        now[1] = now[1] + dy[d]
    
    d = (d+1) % 4
    rotate += 1

print(answer)
    


        

         
         


