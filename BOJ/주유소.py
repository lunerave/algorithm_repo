n = int(input())

dis = list(map(int, input().split()))

loc = list(map(int, input().split()))

answer = 0 

prev = -1

idx = 0

for l in loc:
    if idx == len(dis):
        break
    if prev == -1:
        answer += l*dis[idx]
        idx += 1
        prev = l
    else:
        if l > prev:
            answer += prev*dis[idx]
            idx += 1
        else:
            answer += l*dis[idx]
            idx += 1
            prev = l

print(answer)