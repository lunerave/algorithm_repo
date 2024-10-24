def solution(sequence, k):
    answer = [0, 1000000]
    
    left = 0
    right = 0
    sum_s = sequence[0]
    s_len = len(sequence)
    
    
    while 1:
        if sum_s < k:
            right += 1
            if right >= s_len:
                break
            sum_s += sequence[right]
        elif sum_s > k:
            sum_s -= sequence[left]
            left += 1
        else:
            if right - left < answer[1] - answer[0]:
                answer[0] = left
                answer[1] = right
            right += 1
            if right >= s_len:
                break
            sum_s += sequence[right]
            
    return answer