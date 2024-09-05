dice = [0] * 6

def turn(command):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if command == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = f, b, a, c, e, d
    elif command == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, d, f, e, a
    elif command == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, d, c, e, a, f
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c , b, d, f


N, M, x, y, k = list(map(int, input().split()))

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

for c in comm:
    if c == 1:
        y += 1
        if y >= M:
            y -= 1
            continue
        turn(1)
        if board[x][y] == 0:
            board[x][y] = dice[3]
            print(dice[0])
        else:
            dice[3] = board[x][y]
            board[x][y] = 0
            print(dice[0])
    elif c == 2:
        y -= 1
        if y < 0:
            y += 1
            continue
        turn(2)
        if board[x][y] == 0:
            board[x][y] = dice[3]
            print(dice[0])
        else:
            dice[3] = board[x][y]
            board[x][y] = 0
            print(dice[0])
    elif c == 3:
        x -= 1
        if x < 0:
            x += 1
            continue
        turn(3)
        if board[x][y] == 0:
            board[x][y] = dice[3]
            print(dice[0])
        else:
            dice[3] = board[x][y]
            board[x][y] = 0
            print(dice[0])
    else:
        x += 1
        if x >= N:
            x -= 1
            continue
        turn(4)
        if board[x][y] == 0:
            board[x][y] = dice[3]
            print(dice[0])
        else:
            dice[3] = board[x][y]
            board[x][y] = 0
            print(dice[0])
    

