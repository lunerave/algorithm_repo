from collections import defaultdict

n = int(input())

for _ in range(n):
    s = input()
    k = int(input())
    answer1 = 10000
    answer2 = 0

    dic = defaultdict(list)

    for i in range(len(s)):
        c = s[i]
        if c not in dic:
            dic[c] = [i]
        else:
            dic[c].append(i)
        
        if len(dic[c]) >= k:
            answer1 = min(answer1, dic[c][len(dic[c])-1] - dic[c][len(dic[c])-k] + 1)
    
    if answer1 == 10000:
        print(-1)
        continue

    dic2 = defaultdict(list)

    for i in range(len(s)):
        c = s[i]
        if c not in dic2:
            dic2[c] = [i]
        else:
            dic2[c].append(i)
        
        if len(dic2[c]) >= k:
            answer2 = max(answer2, dic2[c][len(dic2[c])-1] - dic2[c][len(dic2[c])-k] + 1)
    
    print(answer1, answer2)
