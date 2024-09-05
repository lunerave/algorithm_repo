from collections import deque

n, m = list(map(int, input().split()))
global answer, d
answer = 0
room = []

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

x, y, d = list(map(int, input().split()))

for _ in range(n):
    room.append(list(map(int, input().split())))

def turn():
    global d

    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2

def check(x, y):
    if x + 1 < n:
        if room[x+1][y] == 0:
            return True
    
    if x - 1 >= 0:
        if room[x-1][y] == 0:
            return True
    
    if y + 1 < m:
        if room[x][y+1] == 0:
            return True
    
    if y - 1 >= 0:
        if room[x][y-1] == 0:
            return True
    
    return False

q = deque()
q.append((x, y))

while q:
    x, y = q.popleft()

    if room[x][y] == 0:
        room[x][y] = 2
        answer += 1

    if check(x, y):
        turn()
        while room[x + move[d][0]][y + move[d][1]] != 0:
            turn()
        nx = x + move[d][0]
        ny = y + move[d][1]
        q.append((nx, ny))
    else:
        nx = x - move[d][0]
        ny = y - move[d][1]

        if 0 < nx < n - 1 and 0 < ny < m - 1 and room[nx][ny] != 1:
            q.append((nx, ny))
        else:
            print(answer)
            exit(0)
            
            


        

