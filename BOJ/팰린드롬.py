# BOJ 10942
import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

m = int(input())

dp = [[0]*n for _ in range(n)]

# start, end 사이의 값이 팰린드롬인지 저장되어 있는 값을 통해 탐색
for i in range(n):
    # 대각선 순서대로 값을 갱신해야 start, end 사이의 값을 정확히 얻어낼 수 있다.
    for start in range(n-i):
        end = start + i
        # start, end 같다면 반드시 팰린드롬
        if end==start:
            dp[start][end] = 1
        else:
            if numbers[start] == numbers[end]:
                # start바로 다음 end이고 같다면 팰린드롬
                if (start + 1) == end:
                    dp[start][end] = 1
                # start와 end 사이가 팰린드롬인지 확인
                elif dp[start+1][end-1] == 1:
                    dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
