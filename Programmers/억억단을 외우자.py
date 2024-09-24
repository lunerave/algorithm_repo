def solution(e, starts):
    numbers = [0 for _ in range(e+1)]
    numbers[1] = 1
    
    min_s = min(starts)
    
    # 약수의 갯수를 구하여 각 numbers에 저장
    for i in range(1, e + 1):
        if i * i <= e:
            numbers[i*i] += 1
        for j in range(i+1, e + 1):
            n = i * j
            # n > e라면 이미 타겟 넘버를 넘어감
            if n > e:
                break
            numbers[n] += 2
    
    big_numbers = [i for i in range(e+1)]
    # 약수의 갯수가 가장 큰 값 중 작은 값을 기준으로 정렬

    for i in range(e-1, min_s-1, -1):
        if numbers[i] < numbers[big_numbers[i+1]]:
            big_numbers[i] = big_numbers[i+1]
            
    return [big_numbers[s] for s in starts]
    