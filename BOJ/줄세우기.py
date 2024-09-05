n = int(input())

for i in range(n):
    line = list(map(int, input().split()))
    line = line[1:]
    answer = 0
    temp = []

    for l in line:
        if len(temp) == 0:
                temp.append(l)
                continue
        for j in range(len(temp)):
            if temp[j] > l:
                answer += len(temp) - j
                temp = temp[:j] + [l] + temp[j:]
                break

            if j == len(temp)-1:
                 temp.append(l)

    print(i+1, answer)

