N, K = map(int, input().split())

temp = []

rank = 1

temp_count = 0

for _ in range(N):
    temp.append(list(map(int, input().split())))

temp.sort(key = lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    if temp[i][0] == K:
        idx = i

for i in range(N):
    if temp[idx][1:] == temp[i][1:]:
        print(i+1)
        break
        

            



        