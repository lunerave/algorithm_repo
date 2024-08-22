n, m , l, k = map(int, input().split())

stars = []

for _ in range(k):
    x, y = map(int, input().split())
    stars.append((x, y))

# 트램펄린에 떨어질 가장 많은 별 수
max_stars = 0

# 두 개의 별 위치를 기준으로 트램펄린을 설치해서 가장 많은 별의 수를 받는 경우를 탐색한다
for i in range(k):
    for j in range(k):
        count = 0
        # 트램펄린이 설치될 가장 합리적인 x, y 좌표 = 두 별자리의 가장 작은 x, y 좌표
        sx, sy = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

        # 해당 위치에서 떨어질 별의 수 탐색
        for x, y in stars:
            if sx <= x <= sx + l and sy <= y <= sy + l:
                count += 1
        
        max_stars = max(max_stars, count)

print(k - max_stars)