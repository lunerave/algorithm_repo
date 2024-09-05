while True:
    s = input()

    if s == 'end':
        break

    # 모음 카운터
    v_count = 0
    three = 0
    continue_flag = 0

    for c in s:
        if three == 0:
            prev = c
        else:
            if prev == c and (c != 'e' and c != 'o'):
                print("<"+s+"> is not acceptable.")
                continue_flag = 1
                break
            else:
                prev = c
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u':
            v_count += 1
            if three == 0:
                three += 1
            elif v_flag == 1:
                three += 1
            elif v_flag == 0:
                three = 1
            
            v_flag = 1
        else:
            if v_flag == 0:
                three += 1
            else:
                three = 1
            v_flag = 0
        
        if three == 3:
            print("<"+s+"> is not acceptable.")
            continue_flag = 1
            break

    
    if continue_flag == 1:
        continue
    
    if v_count == 0:
        print("<"+s+"> is not acceptable.")
        continue
    
    print("<"+s+"> is acceptable.")
    
            


