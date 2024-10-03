n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

# 바로 다음 행렬과의 곱셈 먼저 처리
for i in range(n-1):
    dp[i][i+1] = matrix[i][0]*matrix[i+1][1]*matrix[i+1][0]

# AxB 행렬과 BxC 행렬 곱셈 횟수는 AxBxC
# i에서 j 사이 임의 k를 이용해 dp[i][j] 탐색
# dp[i][j] = dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1] 의 값들 중 최소값
for l in range(2, n):
    i = 0
    j = l

    while j < n:
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])

        i += 1
        j += 1

print(dp[0][n-1])