n, t, p = map(int, input().split())

same = 0

if n == 0:
    print(1)
    exit(0)

rank = list(map(int, input().split()))


for i in range(len(rank)):
    if t == rank[i]:
        same += 1
    if i+1 <= p:
        if rank[i] < t:
            print(i+1-same)
            exit(0)

if len(rank) < p:
    print(len(rank)+1-same)
else:
    print(-1)




