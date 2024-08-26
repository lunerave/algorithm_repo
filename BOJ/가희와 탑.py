n, a, b = map(int, input().split())

answer = []

# 왼쪽 입장에서의 건물 저장
for i in range(1, a):
    answer.append(i)

# 왼쪽 오른쪽 입장에서 가장 큰 건물 저장
answer.append(max(a, b))

# 오른쪽 입장에서 보이는 건물 저장
for i in range(b-1, 0, -1):
    answer.append(i)

# 저장된 건물 수가 주어진 수보다 크면 불가능
if len(answer) > n:
    print(-1)
else:
    # 첫 번째 건물 저장
    answer_str = str(answer[0]) + " "

    # 남는 건물의 수 만큼 1의 높이 건물 저장 -> 사전 순 조건 충족
    for i in range(n-len(answer)):
        answer_str += "1 "
    
    # 나머지 건물 저장
    for i in range(1, len(answer)):
        if i != len(answer)-1:
            answer_str += str(answer[i]) + " "
        else:
            answer_str += str(answer[i])

    print(answer_str)