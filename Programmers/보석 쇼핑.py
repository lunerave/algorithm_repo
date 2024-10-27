def solution(gems):
    answer = []
    
    gem_len = len(set(gems))
    
    left, right = 0, 0
    
    h = {gems[0]: 1}
    
    while left < len(gems) and right < len(gems):
        if len(h) == gem_len:
            if answer == []:
                answer = [left, right]
            elif right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                h[gems[left]] -= 1
                if h[gems[left]] == 0:
                    del h[gems[left]]
                left += 1
        else:
            right += 1
            
            if right == len(gems):
                break
                
            if gems[right] in h:
                h[gems[right]] += 1
            else:
                h[gems[right]] = 1

    
    return [answer[0]+1, answer[1]+1]
                