import copy

n, m = map(int, input().split())

# cctv가 탐색해야할 모든 방향 저장
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maps = []
cctv = []

for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            cctv.append((maps[i][j], i, j))

# dfs 탐색을 통해 각 임시 배열 사각지대 갱신
def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = '#'
                elif board[nx][ny] == 6:
                    break
            else:
                break


def dfs(depth, board):
    global answer

    # 모든 cctv 탐색 완료
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)

        answer = min(answer, count)
        return
    
    temp = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        # 임시 배열 원복 다음 cctv 모드 탐색
        temp = copy.deepcopy(board)

answer = 10e9
dfs(0, maps)
print(answer)



