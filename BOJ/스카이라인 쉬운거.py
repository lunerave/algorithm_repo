n = int(input())

# 마지막 건물을 세기 위해 추가
skyline = [0]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 이전 건물보다 높이가 큰 건물을 만나면 새로운 건물
    if y > skyline[-1]:
        answer += 1
        skyline.append(y)
    else:
        # 작거나 같은 건물을 만나면 이전 건물의 스카이라인이 끝남
        while skyline[-1] > y:
            skyline.pop()

        # 남아있는 건물보다 현재 건물이 높이가 크면 새로운 건물
        # 같은 높이라면 새로운 건물이 아니므로 그냥 pass한다
        if y > skyline[-1]:
            answer += 1
            skyline.append(y)

print(answer)


