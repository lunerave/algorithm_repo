n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

# 깊은 복사를 통해서 기존 스위치의 상태에 영향을 주지 않고 임시 전구 배열 갱신
bulb_copy = bulb[:]

answer = 10e9

press = 0

# 타겟 전구 배열을 찾았는지 알기 위한 flag
finished = 0

# 처음부터 타겟 전구와 같을 경우
if bulb == target:
    print(0)
    exit()

# 첫번째 스위치를 눌리지 않은 케이스
# 탐색 중인 전구의 이전 전구의 상태를 기준으로 현재 스위치를 누를 지 선택
for i in range(1, n):
    if bulb_copy[i-1] == target[i-1]:
        continue

    press += 1

    for j in range(i-1, i+2):
        if j < n:
            bulb_copy[j] = 1 - bulb_copy[j]
    
    if bulb_copy == target:
        finished = 1
        break

if finished == 1:
    answer = min(answer, press)

# 첫번째 전구 스위치 누른 케이스
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

press = 1

finished = 0

bulb_copy = bulb[:]

for i in range(1, n):
    if bulb_copy[i-1] == target[i-1]:
        continue

    press += 1

    for j in range(i-1, i+2):
        if j < n:
            bulb_copy[j] = 1 - bulb_copy[j]
    
    if bulb_copy == target:
        finished = 1
        break

if finished == 1:
    answer = min(answer, press)

if answer != 10e9:
    print(answer)
else:
    print(-1)



    

