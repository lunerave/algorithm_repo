import sys
input = sys.stdin.readline

def f(a, b):
  if b == 1:
    return a 
  elif b % 2 == 0 :
    t = f(a, b/2)
    return t * t % 1000000007
  else:
    t = f(a, (b-1)/2)
    return t * t * a % 1000000007

f_virus, g_rate, time = map(int, input().split())

time_zone = time * 10

f_virus = f_virus * f(g_rate, time_zone) % 1000000007

print(f_virus)