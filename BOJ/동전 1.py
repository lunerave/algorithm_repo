n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)

dp[0] = 1


# 점화식: 각 코인마다 해당 코인을 뺀 값의 경우의 수 만큼 더해주면 된다
for c in coins:
    for i in range(c, k+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[k])