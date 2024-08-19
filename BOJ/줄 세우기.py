n = int(input())

# 최장 수열의 길이를 저장할 배열
dp = [1] * n

numbers = []

for _ in range(n):
    numbers.append(int(input()))

# LIS 최장 수열 길이 알고리즘 활용
for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp)) 
