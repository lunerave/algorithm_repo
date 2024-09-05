n = int(input())

work = []

for _ in range(n):
    work.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i, w in enumerate(work):
    if i + w[0] <= n:
        temp = max(dp[:i+1])
        dp[i+w[0]] = max(dp[i+w[0]], temp + w[1])

print(max(dp))

