s = input()

bomb = input()

# 문자열 저장
stack = []

# 폭발될 문자열의 길이 저장, 이후 문자열 체크에 사용된다
bomb_len = len(bomb)

# 폭발되어야 하는 지 체크
bomb_flag = 1

for c in s:
    # 폭발 문자열의 마지막 문자를 입력 받을 때 탐색 시작
    if c == bomb[-1]:
        # 스택 길이가 최소 폭발 문자열보다 커야함
        if len(stack) >= bomb_len-1:
            # 스택 마지막 원소 인덱스 초기화
            len_stack = len(stack) - 1
            # 폭발 문자열과 스택에 저장되어 있는 문자열 비교
            for i in range(bomb_len-2, -1, -1):
                if stack[len_stack] != bomb[i]:
                    # 폭발 문자열이 아님
                    bomb_flag = 0
                    break
                len_stack -= 1

            # 폭발 문자열이었다면 폭발 시작
            # 아닐 시 초기에 받은 문자열 스택에 저장, flag 초기화
            if bomb_flag == 1:
                for _ in range(bomb_len-1):
                    stack.pop()
            else:
                stack.append(c)
                bomb_flag = 1
        # 조건을 충족하지 못할 시, 스택에 해당 문자열 저장
        else:
            stack.append(c)
    # 폭발 문자열 마지막 문자를 받기 전까지 스택에 저장
    else:
        stack.append(c)

if stack:
    print(''.join(stack))
else:
    print("FRULA")
