def solution(stones, k):
    small = 1
    big = max(stones)
    
    while small <= big:
        mid = (small + big) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
            
                    
        if cnt >= k:
            big = mid - 1
        else:
            small = mid + 1
             
    return small