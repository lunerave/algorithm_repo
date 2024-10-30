import sys
input = sys.stdin.readline

n = int(input())

list = list(map(int, input().split()))

dp = [1] * n

for x in range(1, n):
  find = 0
  for y in range(x):
    if list[x] > list[y]:
      find = max(find, dp[y])
  dp[x] = find + 1

print(max(dp))
  