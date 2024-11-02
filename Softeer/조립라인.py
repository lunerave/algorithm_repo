import sys
input =  sys.stdin.readline

n = int(input())

a_con, b_con, atb, bta = [0] * (n+1), [0] * (n+1), [0] * (n+1), [0] * (n+1)

for i in range(1, n):
  a, b, atb[i], bta[i] = map(int, input().split())
  if i == 1 :
    a_con[i], b_con[i] = a, b
    continue

  check1 = a_con[i-1] + a
  check2 = b_con[i-1] + bta[i-1] + a
  a_con[i] = min(check1, check2)

  check1 = b_con[i-1] + b
  check2 = a_con[i-1] + atb[i-1] + b
  b_con[i] = min(check1, check2)

aN, bN = map(int, input().split())
check1 = b_con[n-1] + bta[n-1] + aN
check2 = a_con[n-1] + aN
a_con[n] = min(check1, check2)

check1 = a_con[n-1] + atb[n-1] + bN
check2 = b_con[n-1] + bN
b_con[n] = min(check1, check2)

print(min(a_con[n], b_con[n]))
