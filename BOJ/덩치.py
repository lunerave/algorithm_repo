n = int(input())

temp = []

for _ in range(n):
    temp.append(list(map(int, input().split())))

for i in range(len(temp)):
    count = 1
    for j in range(len(temp)):
        if i == j:
            continue
        
        if temp[i][0] < temp[j][0] and temp[i][1] < temp[j][1]:
            count += 1
    
    print(count)
