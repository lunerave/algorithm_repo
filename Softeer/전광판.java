import sys
input = sys.stdin.readline

info = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' '  : '0000000'
}

n = int(input())

for _ in range(n):
    a, b = map(str, input().split())

    a_zero = ' ' * (5-len(a)) + a
    b_zero = ' ' * (5-len(b)) + b

    t = 0

    for i in range(5):
        for j in range(7):
            if info[a_zero[i]][j] != info[b_zero[i]][j]:
                t += 1
    print(t)