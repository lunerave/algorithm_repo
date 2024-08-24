n = int(input())

towers = list(map(int, input().split()))

# 각 빌딩에서 볼 수 있는 건물의 수
can_see = [0] * n

# 각 빌딩에서 볼 수 있는 건물 중 가장 가까운 건물
# 같은 거리에 있다면 왼쪽의 건물을 저장해야한다
near_building = [10e9] * n

left = []

for i in range(n):
    # 현재 건물보다 낮은 건물은 제거한다
    while left and towers[left[-1]] <= towers[i]:
        left.pop()

    # 남아있는 건물은 볼 수 있는 건물이 된다
    can_see[i] = len(left)

    # 왼쪽편의 볼 수 있는 건물을 세는 중이므로, 
    # 가장 가까운 건물은 스택 가장 위에 저장되어 있다
    if left:
        near_building[i] = left[-1]
    
    left.append(i)

right = []

for i in range(n-1, -1, -1):
    while right and towers[right[-1]] <= towers[i]:
        right.pop()

    can_see[i] += len(right)

    # 현재 저장되어 있는 가까운 건물과 비교하여 더 가까운지 판별
    if right:
        if abs(i - right[-1]) < abs(i - near_building[i]):
            near_building[i] = right[-1]
    
    right.append(i)

for i in range(n):
    if can_see[i] > 0:
        print(can_see[i], near_building[i] + 1)
    else:
        print(0)


     

