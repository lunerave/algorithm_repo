from collections import deque

INF = float('inf')
dp = [INF] * 101

# 각 dp에 해당 성냥 개수로 만들 수 있는 최솟값 저장
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8
dp[8] = 10

# i가 6일때는 0을 추가하는 경우를 생각해야 한다
for num in range(9, 101):
    for i in range(2, 8):
        if i != 6:
            dp[num] = min(dp[num], dp[num-i]*10 + dp[i])
        else:
            dp[num] = min(dp[num], dp[num-i]*10)

n = int(input())

for _ in range(n):
    t = int(input())

    # 성냥 개수가 홀수일 때: 7로 시작하는 것이 가장 크다
    # 8이 안되는 이유: 7을 두 개 넣을 수 있다
    # 성냥 개수가 짝수 일대: 7을 넣는 것보다 1을 2개 넣는게 더 큰 숫자를 만든다
    if t%2 == 1:
        max_num = '7' + '1'*(t//2 -1)
    else:
        max_num = '1' + '1'*(t//2 -1)
    
    print(dp[t], max_num)