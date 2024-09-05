n = int(input())
INF = 10e9

num = list(map(int, input().split()))

op = list(map(int, input().split()))
oper = ['+'] * op[0] + ['-'] * op[1] + ['*'] * op[2] + ['/'] * op[3]

length = len(oper)

visited = [0] * length

per = []

def permutations(n ,arr):
    global oper
    if len(arr) == n:
        per.append(arr)
        return
    for i in range(len(oper)):
        if not visited[i]:
            visited[i] = 1
            permutations(n, arr + [oper[i]])
            visited[i] = 0

permutations(length, [])

mx_answer = -INF
mn_answer = INF

for p in per:
    now = num[0]
    idx = 1
    for op in p:
        if op == '+':
            now += num[idx]
            idx += 1
        elif op == '-':
            now -= num[idx]
            idx += 1
        elif op == '*':
            now *= num[idx]
            idx += 1
        else:
            if now < 0:
                now = -(-now // num[idx])
                idx += 1
            else:
                now //= num[idx]
                idx += 1
    mx_answer = max(mx_answer, now)
    mn_answer = min(mn_answer, now)

print(mx_answer)
print(mn_answer)



