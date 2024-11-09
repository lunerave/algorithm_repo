
#플로이드 와샬 사용 각 정점에서 다른 정점으로 이어져있는지 확인한다

def solution(n, results):
    answer = 0
    
    fw = [[0 for _ in range(n)] for _ in range(n)]
    
    for win, loose in results:
        win -= 1
        loose -= 1
        fw[win][loose] = 1
        fw[loose][win] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if fw[i][j] == 0:
                    if fw[i][k] == fw[k][j]:
                        fw[i][j] = fw[i][k]
                
    
    for i in range(n):
        if fw[i].count(0) == 1:
            answer += 1
    
    return answer