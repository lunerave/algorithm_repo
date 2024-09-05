n = int(input())

who = [-1] * 1001

who[1] = 1
who[2] = 0
who[3] = 1

for i in range(4, n+1):
    if who[i-1] == 1 or who[i-3] == 1:
        who[i] = 0
    else:
        who[i] = 1

if who[n] == 1:
    print('SK')
else:
    print('CY')
    