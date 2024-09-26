# import sys
# sys.setrecursionlimit(10**9)

# n = int(input())

# memo = [0] + [1] + [None] * (n - 1)

# def fib(n):
#     if memo[n] != None:
#         return memo[n]
    
    
#     temp = (fib(n-1) + fib(n-2)) % 1000000
#     memo[n] = temp
#     return memo[n]

# print(fib(n))

## 피보나치를 통해서는 못구하는 문제
## 피사노 주기라는 것을 통해서 해결할 수 있다.

n = int(input())

memo = [0, 1]

mod = 1000000

p = mod // 10*15

for i in range(2, p):
    memo.append((memo[i-1] + memo[i-2])%mod)

print(memo[n%p])
    
