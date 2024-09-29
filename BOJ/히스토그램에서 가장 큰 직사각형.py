while True:
    histo = list(map(int, input().split()))

    if histo[0] == 0:
        break
    
    # histo를 저장해가며 스택을 통해 면적 탐색
    stack = []

    n = histo[0]

    answer = 0

    for i in range(1, n+1):
        # 스택이 비어있다면 히스토 추가
        if not stack:
            stack.append((i, histo[i]))
        else:
            # 추가되는 히스토가 이전 히스토보다 크다면 계속 추가
            if stack[-1][1] <= histo[i]:
                stack.append((i, histo[i]))
            else:
                # 작은 히스토가 나왔다면 이전 히스토 면적 계산 시작
                while stack and stack[-1][1] > histo[i]:
                    last = stack.pop()
                    # 스택이 비어있다면 마지막 블록까지를 탐색 중
                    if not stack:
                        width = i - 1
                    else:# 비어있지 않다면 이전 블록의 위치를 통해 width 계산
                        width = i - stack[-1][0] - 1
                    
                    answer = max(answer, last[1] * width)
                stack.append((i, histo[i]))
    
    # 탐색이 끝나고 스택이 비었는지 확인
    while stack:
        last = stack.pop()
        if not stack:
            width = n
        else:
            width = n - stack[-1][0]
        
        answer = max(answer, width*last[1])
    
    print(answer)