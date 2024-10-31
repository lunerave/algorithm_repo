from collections import deque

n, k = map(int, input().split())
m = len(str(n))

visited = set()
visited.add((n, 0))
q = deque()
q.append((n, 0))
answer = 0

while q:
    this_num, this_k = q.popleft()
    if this_k == k:
        answer = max(answer, this_num)
        continue

    this_num = list(str(this_num))

    for i in range(m-1):
        for j in range(i+1, m):
            if i == 0 and this_num[j] == '0':
                continue
        
            this_num[i], this_num[j] = this_num[j], this_num[i]
            nn = int(''.join(this_num))

            if (nn, this_k+1) not in visited:
                q.append((nn, this_k+1))
                visited.add((nn, this_k+1))
            
            this_num[i], this_num[j] = this_num[j], this_num[i]

if answer == 0:
    answer = -1

print(answer)
