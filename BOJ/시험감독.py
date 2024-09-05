answer = 0

n = int(input())

room = map(int, input().split())

t, bt = map(int, input().split())

for r in room:
    r -= t
    answer += 1
    if r > 0:
        bt_num = r // bt
        if bt * bt_num != r:
            answer += bt_num + 1
        else:
            answer += bt_num

print(answer)

