n = int(input())

numbers = list(map(int, input().split()))

# 탐색과 삭제를 효율적으로 처리하기 위한 set
index = set()

# left -> 탐색 시작 기준점
# right -> 이미 탐색된 지점
left = 0
right = 0

answer = 0

while left < n:
    # right 인덱스로 탐색 중인 요소가 set에 없다면 추가 가능
    if right < n and numbers[right] not in index:
        index.add(numbers[right])
        right += 1
    # 탐색 중인 요소가 set에 있는 경우 left 원소의 경우의 수가 끝남
    # 경우의 수는 set에 저장된 원소의 갯수와 같다
    else:
        answer += len(index)
        index.remove(numbers[left])
        left += 1

print(answer)

