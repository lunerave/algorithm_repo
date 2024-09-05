n = int(input())

cookie = []
r_hand = 0
l_hand = 0
body = 0
r_leg = 0
l_leg = 0

for _ in range(n):
    cookie.append(list(input()))

head = []

for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            head = [i, j]
            break
    
    if head:
        break


heart = [head[0]+1, head[1]]

for i in range(heart[1]+1, n):
    if cookie[heart[0]][i] == '*':
        r_hand += 1
    else:
        break

for i in range(heart[1]-1, -1, -1):
    if cookie[heart[0]][i] == '*':
        l_hand += 1
    else:
        break

for i in range(heart[0]+1, n):
    if cookie[i][heart[1]] == '*':
        body += 1
    else:
        break

for j in range(i, n):
    if cookie[j][heart[1]-1] == '*':
        l_leg += 1
    else:
        break

for j in range(i, n):
    if cookie[j][heart[1]+1] == '*':
        r_leg += 1
    else:
        break

print(heart[0]+1, heart[1]+1)
print(l_hand, r_hand, body, l_leg, r_leg)

