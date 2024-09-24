def solution(e, starts):
    numbers = [0 for _ in range(e+1)]
    numbers[1] = 1
    
    min_s = min(starts)
    
    for i in range(1, e + 1):
        if i * i <= e:
            numbers[i*i] += 1
        for j in range(i+1, e + 1):
            n = i * j
            if n > e:
                break
            numbers[n] += 2
        
    big_numbers = [i for i in range(e+1)]
    
    for i in range(e-1, min_s-1, -1):
        if numbers[i] < numbers[big_numbers[i+1]]:
            big_numbers[i] = big_numbers[i+1]
            
    return [big_numbers[s] for s in starts]
    