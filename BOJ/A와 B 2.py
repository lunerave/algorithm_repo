from collections import deque

S = input()
T = input()

q = deque()

q.append(T)

flag = 0
count = 0

while q:
    t = q.popleft()
    count += 1

    if t == S:
        flag = 1
        break

    if t[0] == 'B':
        nt = t[1:]
        nt = list(nt)
        nt.reverse()
        nt = ''.join(nt)

        if len(nt) >= len(S):
            q.append(nt)
    
    if t[len(t)-1] == 'A':
        nt = t[:len(t)-1]

        if len(nt) >= len(S):
            q.append(nt)

if flag == 1:
    print(1)
else:
    print(0)




