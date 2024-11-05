import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0

line = []

line = list(input())

check = [0] * n

for i in range(n):
    if line[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j >= n or i == j:
                continue
            if check[j] == 0 and line[j] == 'H':
                answer += 1
                check[j] = 1
                break

print(answer)
        