n, c = map(int, input().split())

house = []

for _ in range(n):
    house.append(int(input()))

# 탐색을 위해 정렬
house.sort()

answer = 0

# 최소 거리 초기화
left = 1
# 최대 거리 초기화
right = house[-1] - house[0]

while left <= right:
    mid = (left + right) // 2

    # 첫 번째 집부터 탐색 시작
    target = house[0]

    # 와이파이 무조건 첫 번째 집에는 설치가 되야 한다.
    count = 1

    for i in range(1, n):
        # 이전 와이파이 집과의 거리 확인
        if house[i] >= target + mid:
            count += 1
            target = house[i]
    
    # 와이파이가 많이 설치됨 -> 집 간의 거리가 더 멀어져야 함 
    # 와이파이가 적게 설치됨 -> 집 간의 거리가 더 좁아져야 함
    if count >= c:
        left = mid + 1
        answer = mid
    elif count < c:
        right = mid - 1

print(answer)
    
