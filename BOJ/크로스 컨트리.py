from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    case = list(map(int, input().split()))

    dic = defaultdict(list)

    lost = []

    for idx, c in enumerate(case):
        dic[c].append(idx+1)
    
    for k in dic.keys():
        if len(dic[k]) < 6:
            lost.append(k)

    idx = 1

    dic = defaultdict(list)

    for c in case:
        if c in lost:
            continue
        else:
            if c not in dic:
                dic[c].append([idx, 1, c])
            else:
                if dic[c][0][1] == 4:
                    dic[c][0].append(idx)
                    dic[c][0][1] += 1
                elif dic[c][0][1] == 5:
                    idx += 1
                    continue
                else:
                    dic[c][0][0] += idx
                    dic[c][0][1] += 1
            idx += 1
    
    temp = []

    for t in dic.values():
        temp.append(t[0])
    
    temp.sort(key=lambda x:(x[0], x[3]))
    print(temp[0][2])
