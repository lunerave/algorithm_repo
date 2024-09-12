n, k = map(int, input().split())

bags = []

for _ in range(n):
    bags.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재 물건 무게보다 탐색하는 가방 무게가 더 큰 지 확인
        if j >= bags[i-1][0]:
            # 가방 무게에서 현재 물건을 뺀 무게만큼의 물건이 더 들어갈 수 있는지 확인
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bags[i-1][0]] + bags[i-1][1])
        else:
            # 현재 물건은 가방에 담을 수 없음
            dp[i][j] = dp[i-1][j]

print(dp[n][k])