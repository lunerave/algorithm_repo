while True:
    tic = input()

    if tic == 'end':
        break
    
    tic = list(tic)

    xcount = 0
    ocount = 0
    xtic = 0
    otic = 0
    win = -1

    for t in tic:
        if t == 'X':
            xcount += 1
        elif t == 'O':
            ocount += 1
    
    if ocount == xcount or xcount == ocount+1:
        if xcount == ocount:
            win = 1
        else:
            win = 0

        if tic[0] == tic[1] == tic[2]:
            if tic[0] == 'X':
                xtic += 1
            elif tic[0] == 'O':
                otic += 1
        
        if tic[3] == tic[4] == tic[5]:
            if tic[3] == 'X':
                xtic += 1
            elif tic[3] == 'O':
                otic += 1
        
        if tic[6] == tic[7] == tic[8]:
            if tic[6] == 'X':
                xtic += 1
            elif tic[6] == 'O':
                otic += 1
        
        if tic[0] == tic[3] == tic[6]:
            if tic[0] == 'X':
                xtic += 1
            elif tic[0] == 'O':
                otic += 1

        if tic[1] == tic[4] == tic[7]:
            if tic[1] == 'X':
                xtic += 1
            elif tic[1] == 'O':
                otic += 1

        if tic[2] == tic[5] == tic[8]:
            if tic[2] == 'X':
                xtic += 1
            elif tic[2] == 'O':
                otic += 1

        if tic[0] == tic[4] == tic[8]:
            if tic[0] == 'X':
                xtic += 1
            elif tic[0] == 'O':
                otic += 1

        if tic[2] == tic[4] == tic[6]:
            if tic[2] == 'X':
                xtic += 1
            elif tic[2] == 'O':
                otic += 1

        if otic > 0 and win == 1:
            print("invalid")
            continue

        if otic > 0 and xcount + ocount == 9:
            print("invalid")
            continue

        if otic == 0 and xtic == 0:
            if xcount + ocount != 9:
                print("invalid")
                continue

        if otic > 0 and xtic > 0:
            print("invalid")
            continue

        print("valid")
    else:
        print("invalid")


    






    
        

