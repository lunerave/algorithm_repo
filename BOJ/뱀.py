from collections import deque

def change_direct(command):
    global dx, dy
    if dx == 0 and dy == 1:
        if command == 'L':
            dx, dy = -1, 0
        else:
            dx, dy = 1, 0

    elif dx == 1 and dy == 0:
        if command == 'L':
            dx, dy = 0, 1
        else:
            dx, dy = 0, -1
        
    elif dx == -1 and dy == 0:
        if command == 'L':
            dx, dy = 0, -1
        else:
            dx, dy = 0, 1
        
    elif dx == 0 and dy == -1:
        if command == 'L':
            dx, dy = 1, 0
        else:
            dx, dy = -1, 0

answer = 0

n = int(input())

a = int(input())

apple = []

for _ in range(a):
    apple.append(list(map(int, input().split()))) 

d = int(input())

direct = deque()

for _ in range(d):
    direct.append(list(input().split()))

global dx, dy

dx, dy = 0, 1

x, y = 0, 0

snake = deque()
snake.append((x, y))

while True:
    x += dx
    y += dy

    answer += 1
    
    if len(direct) != 0:
        if answer == int(direct[0][0]):
            change_direct(direct[0][1])
            direct.popleft()

    if 0 > x or x >= n or 0 > y or y >= n:
        print(answer)
        exit(0)  

    if (x, y) in snake:
        print(answer)
        exit(0)

    if [x+1, y+1] not in apple:
        snake.popleft()
    else:
        apple.remove([x+1, y+1])


    snake.append((x, y))


    
    

