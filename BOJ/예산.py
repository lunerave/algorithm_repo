n = int(input())

budgets = list(map(int, input().split()))

mb = int(input())

budgets.sort()

left = 1
right = budgets[n-1]
answer = 0

while left <= right:
    now = 0
    mid = (left + right) // 2
    
    for i in range(n):
        if budgets[i] < mid:
            now += budgets[i]
        else:
            now += mid * (n-i)
            break
    
    if now <= mb:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
    

print(answer)

