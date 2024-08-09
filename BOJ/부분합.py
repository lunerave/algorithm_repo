n, s = map(int, input().split())

numbers = list(map(int, input().split()))

# 최소 길이를 구해야 하므로 max 수로 초기화
answer = 10e9

# 투 포인터 방식을 활용하기 위한 left, right 인덱스
left = 0
right = 0

# 현재까지의 합을 저장하는 변수
ns = 0

# right가 끝 부분의 수를 합쳤을 때, right가 n과 같아짐
while right <= n:
    # 문제 조건 충족
    if ns >= s:
        answer = min(answer, right - left)
        # 최소 길이 탐색 시작
        ns -= numbers[left]
        left += 1
    else:
        if right != n:
            ns += numbers[right]
        
        # 끝부분까지 탐색
        right += 1

if answer == 10e9:
    print(0)
else:
    print(answer)
    

