import heapq
import sys
input = sys.stdin.readline

n = int(input())

# 왼쪽 힙은 최대힙, 오른쪽 힙은 최소힙으로 구성한다.
# 왼쪽 힙에는 중간값보다 작거나 같은 값, 오른쪽 힙에는 중간값보다 큰 값이 들어간다
leftHeap = []
rightHeap = []

for i in range(n):
    num = int(input())

    # 두 힙의 길이가 같으면 왼쪽 heap에 추가
    # 다르면 오른쪽 heap에 추가
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    # 왼쪽 힙에 오른쪽 힙의 루트 값보다 큰 값이 들어있다면 작은 수가 아닌 큰 수가 출력된다
    # 따라서, 두 값을 스왑해줘야한다.
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        toRight = heapq.heappop(leftHeap)
        toLeft = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -toLeft)
        heapq.heappush(rightHeap, -toRight)

    print(-leftHeap[0])
