from collections import deque

tc = int(input())

# 문제 조건의 ASCII 순으로 나열하기 위한 순서로 저장
operations = [' ', '+', '-']

for t in range(tc):
    n = int(input())

    answer = []

    q = deque()

    # 무조건 1부터 시작
    q.append((1, '1'))

    while q:
        now, formula = q.popleft()

        # eval를 사용하면 스트링으로 나열된 식의 결과값을 반환받음
        if now == n:
            ans = eval(formula.replace(' ', ''))

            if ans == 0:
                answer.append(formula)

            continue

        for i in range(3):
            nf = formula + operations[i] + str(now+1)

            if now <= n:
                q.append((now+1, nf))

    for a in answer:
        print(a)
    
    if t != tc-1:
        print()


    
            
                



    
