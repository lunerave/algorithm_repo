def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    
    islands = set([costs[0][0]])
    
    while len(islands) != n:
        for cost in costs:
            if cost[0] in islands and cost[1] in islands:
                continue
            if cost[0] in islands or cost[1] in islands:
                islands.update((cost[0], cost[1]))
                answer += cost[2]
                break
    
    
    return answer