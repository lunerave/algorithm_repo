n = int(input())

switch = list(map(int, input().split()))

students_num = int(input())

for _ in range(students_num):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for i in range(num, n+1, num):
            if switch[i-1] == 1:
                switch[i-1] = 0
            else:
                switch[i-1] = 1
    else:
        num -= 1

        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0

        left = num - 1
        right = num + 1
        while left>=0 and right<n:
            if switch[left] == switch[right]:
                if switch[left] == 0:
                    switch[left] = 1
                    switch[right] = 1
                else:
                    switch[left] = 0
                    switch[right] = 0
            else:
                break
            left -= 1
            right += 1
    
for i in range(n):
    print(switch[i], end='')
    if (i + 1) % 20 == 0: # 줄의 마지막일 때 19, 39 -> 줄바꿈
        print()
    else:  # 줄의 마지막이 아닐 때 -> 띄어쓰기
        print(' ', end='')


            
