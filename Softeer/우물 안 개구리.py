import sys
input = sys.stdin.readline

people, relation = map(int, input().split())

data = list(map(int, input().split()))

answer_list = [1] * people

for x in range(relation):
  a, b = map(int, input().split())
  if data[a-1] > data[b-1]:
    answer_list[b-1] = 0
  elif data[a-1] < data[b-1]:
    answer_list[a-1] = 0
  elif data[a-1] == data[b-1]:
    answer_list[a-1] = 0
    answer_list[b-1] = 0

answer = answer_list.count(1)

print(answer)
      
  