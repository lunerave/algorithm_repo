import heapq
# 인풋을 빨리 받기 위한 sys 없으면 시간 초과
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

gems = []

for _ in range(n):
    gems.append(list(map(int, input().split())))

# 보석들을 무게와 가격 오름차순으로 정렬
# 가방에 들어갈 수 있는 보석들을 순차적으로 탐색하기 위함
gems.sort()

bags = []

# 작은 가방부터 보석 탐색 
for _ in range(k):
    heapq.heappush(bags, int(input()))

answer = 0

# 담을 수 있는 보석 저장
tmp_bag = []

while bags:
    bag = heapq.heappop(bags)

    # 현재 보석이 현재 가방에 담길 수 있는지 확인
    # 현재 가방에 담길 수 있다면 다음 가방에도 반드시 담길 수 있다
    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp_bag, -gems[0][1])
        heapq.heappop(gems)
    
    # 가장 가치가 높은 보석 가방에 저장
    if tmp_bag:
        answer += -heapq.heappop(tmp_bag)


print(answer)
