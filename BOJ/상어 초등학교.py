N = int(input())
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

st_num = N**2

fr = [[] for _ in range(st_num+1)]
order = []

seat = [[None] * N for _ in range(N)]

for _ in range(st_num):
    st, st1, st2, st3, st4 = list(map(int, input().split()))
    order.append(st)
    fr[st] = [st1, st2, st3, st4]

for st in order:
    temp = []
    for i in range(N):
        for j in range(N):
            if seat[i][j] == None:
                cnt = 0
                n_cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0<=nx<N and 0<=ny<N:
                        if seat[nx][ny] == None:
                            n_cnt += 1
                        else:                 
                            if seat[nx][ny] in fr[st]:
                                cnt += 1
                temp.append((cnt, n_cnt, i, j))
    temp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    seat[temp[0][2]][temp[0][3]] = st

satisfy = [0, 1, 10, 100, 1000]

for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0<=nx<N and 0<=ny<N:
                if seat[nx][ny] in fr[seat[i][j]]:
                    cnt += 1
        answer += satisfy[cnt]

print(answer)







