n = int(input())

buildings = list(map(int, input().split()))

answer = 0


# 건물 기준 좌측 건물을 탐색할 때는 점차 기울기가 작아져야 관측 가능
# 건물 기준 우측 건물을 탐색할 때는 점차 기울기가 커져야 관측 가능
for i in range(n):
    last = 10e9
    count = 0
    if i != 0:
        for l in range(i-1, -1, -1):
            now = (buildings[i] - buildings[l]) / (i - l)
            if now < last:
                count += 1
                last = now
    last = -10e9
    if i != n-1:
        for r in range(i+1, n):
            now = (buildings[i] - buildings[r]) / (i - r)
            if now > last:
                count += 1
                last = now
    
    answer = max(answer, count)

print(answer)


            
