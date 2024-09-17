topni = []

for _ in range(4):
    topni.append(list(map(int, input())))

n = int(input())

# 톱니바퀴를 방향에 맞춰 회전
def rotate(tn, d):
    # 역방향 회전
    if d == -1:
        tn.append(tn.pop(0))
    else: # 정방향 회전
        t = tn.pop()
        tn.insert(0, t)

# 톱니바퀴 기준 좌측 톱니바퀴 회전 가능 탐색
def left(idx, d):
    if idx < 0:
        return
    
    if topni[idx][2] != topni[idx+1][6]:
        left(idx-1, -d)
        rotate(topni[idx], d)

# 톱니바퀴 기준 오른쪽 톱니바퀴 회전 가능 탐색
def right(idx, d):
    if idx > 3:
        return
    
    if topni[idx][6] != topni[idx-1][2]:
        right(idx+1, -d)
        rotate(topni[idx], d)


for _ in range(n):
    tn, d = map(int, input().split())

    tn -= 1

    # 좌측, 우측 탐색 후 회전 -> 회전 방향이 바뀌기 때문에 -d
    left(tn-1, -d)
    right(tn+1, -d)

    # 기존 톱니바퀴 회전
    rotate(topni[tn], d)

answer = 0

for i in range(4):
    if topni[i][0] == 1:
        answer += 2 ** i
    
print(answer)


