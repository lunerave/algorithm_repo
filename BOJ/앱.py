n, m = map(int, input().split())

answer = 2**31

apps = list(map(int, input().split()))

cost = list(map(int, input().split()))

# dp 탐색의 길이 정의
length = sum(cost)+1

dp = [[0]*length for _ in range(n+1)]

for i in range(n):
    byte = apps[i]
    c = cost[i]
    for j in range(length):
        # j가 c보다 작다면, 현재 처리할 수 없음
        if j < c:
            dp[i][j] = dp[i-1][j]
        else: # 이전 단계와 현재 바이트를 더한 값 비교해서 가장 큰 값 저장
            dp[i][j] = max(dp[i-1][j], byte + dp[i-1][j-c])
        
        # 저장된 바이트 값이 원하는 바이트 값보다 크거나 같다면 최소 비용 갱신
        if dp[i][j] >= m:
            answer = min(answer, j)

print(answer)
