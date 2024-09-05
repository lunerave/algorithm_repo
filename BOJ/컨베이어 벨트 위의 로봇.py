n, k = map(int, input().split())

belt = list(map(int, input().split()))

answer = 0

down = n - 1

count = 0

robot = [0] * n

while count < k:
    b_l = belt.pop()
    belt = [b_l] + belt
    r_l = robot.pop()
    if r_l == 1:
        r_l = 0
    robot = [r_l] + robot
    
    for i in range(n-1, -1, -1):
        if i == n-1:
            robot[i] = 0
        else:
            if robot[i] == 1:
                if robot[i+1] == 1:
                    continue
                if belt[i+1] > 0:
                    robot[i] = 0
                    robot[i+1] = 1
                    belt[i+1] -= 1
                    if belt[i+1] == 0:
                        count+=1


    if belt[0] != 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            count += 1
    
    answer += 1

print(answer)
    
    



    

    

    
            


