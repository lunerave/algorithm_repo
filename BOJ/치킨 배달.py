n, m = map(int, input().split())

answer = 10e9

# 집 저장
home = []

# 치킨집 저장
chick = []

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chick.append((i, j))

visited = [0] * len(chick)


def dfs(idx, cnt):
    global answer

    # 치킨집 갯수가 m 만큼 되었을 때, 치킨 거리 계산
    if cnt == m:
        ans = 0

        # 각각의 집에서 치킨 집까지의 최소 거리 탐색
        for h in home:
            distance = 10e9
            # 각각의 치킨 집 거리 계산 후 최소값 저장
            for c in range(len(chick)):
                if visited[c]:
                    check_num = abs(h[0]-chick[c][0]) + abs(h[1]-chick[c][1])
                    distance = min(check_num, distance)

            ans += distance
        answer = min(ans, answer)

    # 제거하지 않은 치킨집 저장 -> 백트래킹 사용
    for i in range(idx, len(chick)):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, cnt+1)
            visited[i] = 0

dfs(0, 0)

print(answer)
        