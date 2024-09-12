n, l = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0

# 오른쪽 탐색
for i in range(n):
    # 내려갈 때 경사로가 놓인 위치 저장
    index = -1
    # 오른쪽으로 이동했던 발판 갯수 저장 -> 경사로를 놓을 수 있는지 판별하는데 사용
    rcount = 1
    for j in range(n):
        # 오른쪽 탐색

        # 경사로를 사용했다면 경사로 끝 위치까지 이동
        if index != -1:
            if j < index:
                continue
        
        # 마지막 블록까지 도착했다면 이동 가능
        if j == n-1:
            answer += 1
            break

        # 평평한 발판은 이동
        if board[i][j] == board[i][j+1]:
            rcount += 1
        # 위로 이동하는 블록을 만났을 경우 이전 발판이 경사로보다 길거나 같아야한다
        elif board[i][j] < board[i][j+1]:
            # 높이가 2 이상 차이날 경우 불가능
            if board[i][j+1] - board[i][j] > 1:
                break
            if rcount < l:
                break
            rcount = 1
        else: # 밑으로 이동하는 블록을 만났을 경우 이후 발판이 경사로보다 길거나 같아야한다
            # 높이가 2 이상 차이날 경우 불가능
            if board[i][j] - board[i][j+1] > 1:
                break
            # 아래에 있는 블록 갯수 저장
            drcount = 0
            
            for t in range(j+1, n):
                # 경사로 길이만큼 거리가 된다면 이동
                if drcount == l:
                    break
                if board[i][t] == board[i][j+1]:
                    drcount += 1
                else:
                    break
                
                if t == n-1:
                    t += 1
                    break

            if drcount != l:
                break
            else:
                index = t-1
                rcount = 0
            
# 세로 탐색 알고리즘은 위와 같다
for i in range(n):
    index = -1
    vcount = 1
    vdrcount = 1
    downflag = 0
    for j in range(n):
        if index != -1:
            if j < index:
                continue
        if j == n-1:
            answer += 1
            break

        if board[j][i] == board[j+1][i]:
            vcount += 1
        elif board[j][i] < board[j+1][i]:
            if board[j+1][i] - board[j][i] > 1:
                break
            if vcount < l:
                break
            vcount = 1
        else:
            if board[j][i] - board[j+1][i] > 1:
                break
            vdrcount = 0
            for t in range(j+1, n):
                if vdrcount == l:
                    break
                if board[t][i] == board[j+1][i]:
                    vdrcount += 1
                else:
                    break
                
                if t == n-1:
                    t += 1
                    break

            if vdrcount != l:
                break
            else:
                index = t-1
                vcount = 0


print(answer)
        
        


