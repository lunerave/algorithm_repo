import heapq

def solution(jobs):
    answer = 0
    
    start = -1
    
    now = 0
    j = 0
    heap = []
    
    while j != len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))
        if len(heap) > 0:
            task = heapq.heappop(heap)
            start = now
            now += task[0]
            answer += (now - task[1])
            j += 1
        else:
            now += 1
        
    return answer//len(jobs)