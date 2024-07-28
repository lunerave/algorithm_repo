def is_finish(winner):
    key = winner + winner + winner
    if key in [''.join(row) for row in board]: # 가로 검사
        return True
    if key in [''.join([row[i] for row in board]) for i in range(3)]: # 세로 검사
        return True
    if key in [''.join([board[i][i] for i in range(3)]), ''.join([board[j][abs(j - 2)] for j in range(3)])]: # 대각선 검사
        return True
    return False

def is_valid(x, o):
    if (x > 5) or (o > 4):
        print('invalid')
        return
    valid = False
    of, xf = is_finish('O'), is_finish('X')
    if x == o: # O가 이겨야함
        if of and (not xf):
            valid = True
    elif (x - 1) == o: # X가 이김 or 둘다 못이겼지만 가득차야함
        if xf and (not of):
            valid = True
        elif (not of) and (not xf):
            if not any('.' in row for row in board):
                valid = True
    if valid:
        print('valid')
    else:
        print('invalid')

while True:
    board = input().rstrip()
    if board == 'end': break
    x, o = board.count('X'), board.count('O')
    board = [list(board[i:i+3]) for i in range(0, 7, 3)]
    is_valid(x, o)


    






    
        

