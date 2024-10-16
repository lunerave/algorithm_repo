first = ' ' + input()
second = ' ' + input()

dp = [[0] * len(second) for _ in range(len(first))]

# 냅색과 비슷하게 풀이
for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])