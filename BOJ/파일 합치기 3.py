import heapq

t = int(input())

for _ in range(t):
    k = int(input())

    files = list(map(int, input().split()))

    # min 힙으로 변환
    heapq.heapify(files)

    answer = 0

    while files:
        # 작은 수들을 먼저 꺼내와서 더해가면 문제를 해결할 수 있다
        x = heapq.heappop(files)
        y = heapq.heappop(files)

        answer += x + y

        heapq.heappush(files, x+y)

        # 하나 남았을 경우, 탐색이 종료되었음
        if len(files) == 1:
            break
    
    print(answer)

    


    
