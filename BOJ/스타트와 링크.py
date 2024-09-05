
n = int(input())

answer = 10e9

team = []

for _ in range(n):
    team.append(list(map(int, input().split())))

player = [i for i in range(n)]

visited = [0] * len(player)

per = []

def permutations(n, new_arr, new_player):
    if len(new_arr) == n:
        per.append(new_arr)
        return
    for i in range(len(new_player)):
        if visited[i] == 0:
            visited[i] = 1
            permutations(n, new_arr + [new_player[i]], new_player)
            visited[i] = 0

com = []

def combinations(n, new_arr, c):
    if len(new_arr) == n:
        com.append(new_arr)
        return
    for i in range(c, len(player)):
        combinations(n, new_arr + [player[i]], i+1)

player_num = n // 2

combinations(player_num, [], 0)

for i in range((len(com) // 2)):
    com1 = com[i]
    com2 = []
    for p in player:
        if p not in com1:
            com2.append(p)
    c1 = 0
    c2 = 0
    permutations(2, [], com1)
    for x, y in per:
        c1 += team[x][y]
    per = []
    permutations(2, [], com2)
    for x, y in per:
        c2 += team[x][y]
    per = []

    num = abs(c1-c2)
    answer = min(answer, num)

print(answer)