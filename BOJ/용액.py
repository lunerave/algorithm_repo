n = int(input()) 
liquid = list(map(int, input().split()))

left = 0
right = n-1

# ans 초기화
ans = abs(liquid[left] + liquid[right])

# ans에 대한 값을 가지는 liquid element 인덱스 저장
ans_left = left
ans_right = right

# left보다 right가 작거나 같을 시 전체 케이스 탐색 완료
while left < right:
    tmp = liquid[left] + liquid[right]

    # 새로운 ans 값 탐색 완료, ans, ans_left, ans_right 갱신
    if abs(tmp) < ans:
        ans_left = left
        ans_right = right
        ans = abs(tmp)

        if ans == 0:
            break
    
    # tmp가 음수일 때, left 인덱스를 올려 -값을 줄인다
    # tmp가 양수일 때, right 인덱스를 내려 +값을 줄인다
    if tmp < 0:
        left += 1
    else:

        right -= 1

print(liquid[ans_left], liquid[ans_right])




