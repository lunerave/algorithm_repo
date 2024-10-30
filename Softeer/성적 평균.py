import sys
input = sys.stdin.readline

student_num, interval_num = map(int, input().split())

list = list(map(int, input().split()))

for x in range(interval_num):
  left, right = map(int, input().split())
  interval_sum = sum(list[left-1:right])
  print("%0.2f"%(interval_sum/(right-left + 1)))
  