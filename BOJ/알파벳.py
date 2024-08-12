r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(input())

# 가장 긴 경로 저장
ans = 0

# 경로에 같은 알파벳은 올 수 없다
path = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백트래킹 기법을 활용하여 조건에 맞는 모든 경로 탐색
def dfs(x, y, count):
    global ans

    ans = max(ans, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 문제 조건 가지치기
        if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in path:
            # 경로 추가
            path.add(board[nx][ny])
            dfs(nx, ny, count+1)
            # 백트래킹 경로 제거
            path.remove(board[nx][ny])

path.add(board[0][0])
dfs(0, 0, 1)
print(ans)








