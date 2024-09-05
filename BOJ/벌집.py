import math

n = int(input())

start = 1

skip = 1

count = 1

while start <= n:
    start += skip
    skip = 6*count
    count += 1

print(count-1)