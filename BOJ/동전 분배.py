from collections import deque

for _ in range(3):
    n = int(input())

    wallet = {}

    total = 0

    for _ in range(n):
        coin, amount = map(int, input().split())
        wallet[coin] = amount
        total += coin*amount

    # 총 액이 짝수가 아니라면 이미 불가능
    if total % 2 == 1:
        print(0)
        continue
    
    # dp[i] = i원을 만들 수 있는 지 여부
    # 0원은 반드시 만들 수 있다
    dp = [1] + [0] * (total//2)

    for coin in wallet:
        # 동전 중복 사용을 방지하기 위해 역순 탐색
        for target in range(total//2, coin-1, -1):
            # 이 경우 해당 동전을 사용해서 목표 금액을 얻을 수 있다
            if dp[target-coin]:
                for i in range(wallet[coin]):
                    if target + coin*i <= total//2:
                        dp[target + coin*i] = 1

    print(dp[total//2])
            


    


