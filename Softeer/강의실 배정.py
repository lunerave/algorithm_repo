import sys
import heapq

imput = sys.stdin.readline

n = int(input())

list = []

for x in range(n):
  start, end = map(int, input().split())
  heapq.heappush(list, (end, start))

end_time = 0
count = 0

while list:
  a, b = heapq.heappop(list)
  if b >= end_time:
    count += 1
    end_time = a

print(count)
      
  
  