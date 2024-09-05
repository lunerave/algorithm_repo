import math

n = int(input())
m = int(input())

answer = 1000000

zero = 0

light = list(map(int, input().split()))

gap = 0

for i in range(1, m):
    gap = max(gap, math.ceil((light[i]-light[i-1])//2))

for i in range(m):
    while zero < light[i] - gap:
        gap += 1
    zero = light[i] + gap

    if i == m-1:
        while light[i] + gap < n:
            gap += 1

print(gap)
        








