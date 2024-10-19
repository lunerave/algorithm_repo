arr = [[0] * 5 for _ in range(5)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def tornado():
    global arr

    x = len(arr) // 2
    y = len(arr) // 2

    num = 0
    length = 1
    d = 0
    moved = 0
    
    while True:
        for _ in range(length):
            nx = x + dx[d]
            ny = y + dy[d]

            if (nx, ny) == (0, -1):
                return
            
            num += 1
            arr[nx][ny] = num
            x = nx
            y = ny

        moved += 1
        d = (d+1) % 4
        if moved == 2:
            length += 1
            moved = 0

tornado()

for i in range(5):
    print(*arr[i])

