n = int(input())

answer = 0

numbers = list(map(int, input().split()))

# 슬라이딩 윈도우 방식을 사용하기 위해 정렬
numbers.sort()

# 모든 경우의 수 탐색
for i in range(n):
    left = 0
    right = n-1

    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        
        # 위 조건에서 left == right가 될 수 있고 이는 문제의 조건을 벗어남
        if left == right:
            break
        
        # 두 수의 합이 타겟보다 크다: right를 1 내려 낮은 합이 되도록 유도
        # 두 수의 합이 타겟보다 작다: left를 1 올려 높은 합이 되도록 유도
        # 같다: 타겟 넘버 찾음
        if numbers[left] + numbers[right] > numbers[i]:
            right -= 1
        elif numbers[left] + numbers[right] < numbers[i]:
            left += 1
        else:
            answer += 1
            break

print(answer)


