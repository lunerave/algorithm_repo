from collections import deque
import copy

def up(n, board):
    for j in range(n):
        pointer = 0
        for i in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                elif board[pointer][j] == 0:
                    board[pointer][j] = tmp
                else:
                    pointer += 1
                    board[pointer][j] = tmp
            

def down(n, board):
    for j in range(n):
        pointer = n-1
        for i in range(n-1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
                

def left(n, board):
    for i in range(n):
        pointer = 0
        for j in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer] = tmp

def right(n, board):
    for i in range(n):
        pointer = n-1
        for j in range(n-1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp

answer = 0

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

q = deque()

q.append((board, 0))

while q:
    b, c = q.popleft()

    if c == 5:
        for i in range(n):
            for j in range(n):
                if b[i][j] > answer:
                    answer = b[i][j]
        continue

    for i in range(4):
        if i == 0:
            nb = copy.deepcopy(b)
            up(n, nb)
            nc = c + 1
            q.append((nb, nc))
        elif i == 1:
            nb = copy.deepcopy(b)
            down(n, nb)
            nc = c + 1
            q.append((nb, nc))
        elif i == 2:
            nb = copy.deepcopy(b)
            left(n, nb)
            nc = c + 1
            q.append((nb, nc))
        else:
            nb = copy.deepcopy(b)
            right(n, nb)
            nc = c + 1
            q.append((nb, nc))

print(answer)





