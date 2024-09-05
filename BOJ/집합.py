import sys

n = int(input())

S = set()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "add":
        S.add(cmd[1])
    elif cmd[0] == "remove":
        if cmd[1] not in S:
            continue
        S.remove(cmd[1])
    elif cmd[0] == "check":
        if cmd[1] in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.add(cmd[1])
    elif cmd[0] == "all":
        S = set([str(i) for i in range(1, 21)])
    else:
        S = set()


