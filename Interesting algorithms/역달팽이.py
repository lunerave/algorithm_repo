arr = [[0]*5 for _ in range(5)]

n = len(arr)

x, y = 0, 0

def opsnail(x, y):
    global arr
    d = 0

    for i in range(n*n):
        arr[x][y] = i+1
        if d == 0:
            y += 1
            if y == n-1 or arr[x][y+1] != 0:
                d += 1
        elif d == 1:
            x += 1
            if x == n-1 or arr[x+1][y] != 0:
                d += 1
        elif d == 2:
            y -= 1
            if y == 0 or arr[x][y-1] != 0:
                d += 1
        elif d == 3:
            x -= 1
            if x == n-1 or arr[x-1][y] != 0:
                d = 0

opsnail(x, y)

for i in range(5):
    print(*arr[i])
