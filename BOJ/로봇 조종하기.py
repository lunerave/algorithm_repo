n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

# 첫 번째 줄은 위에서 아래로, 우측에서 좌측으로 이동 없이 좌측에서 우측으로 이동밖에 불가능
for i in range(1, m):
    maps[0][i] += maps[0][i-1]

# 두 번째 줄부터 위에서 아래, 좌측에서 우측, 우측에서 좌측 비교 후 최댓값 저장
for i in range(1, n):
    # maps 배열 deep copy -> 기존 배열에 저장된 값에 영향을 주지 않음
    left_to_right = maps[i][:]
    right_to_left = maps[i][:]

    # 좌측에서 우측 경로 탐색
    for j in range(m):
        if j == 0:
            left_to_right[j] += maps[i-1][j]
        else:
            left_to_right[j] += max(maps[i-1][j], left_to_right[j-1])

    # 우측에서 좌측 경로 탐색
    for j in range(m-1, -1, -1):
        if j == m-1:
            right_to_left[j] += maps[i-1][j]
        else:
            right_to_left[j] += max(maps[i-1][j], right_to_left[j+1])

    # 최댓값 저장
    for j in range(m):
        maps[i][j] = max(left_to_right[j], right_to_left[j])


print(maps[n-1][m-1])