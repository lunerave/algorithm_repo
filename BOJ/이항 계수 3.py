n, k = map(int, input().split())

# factorial 함수
def fact(n):
    num = 1

    for i in range(2, n+1):
        num = (num*i) % 1000000007
    
    return num

# 분할 정복 거듭제곱 함수
def square(a, b):
    if b == 1:
        return a % 1000000007
    
    if b % 2 == 0:
        temp = square(a, b//2)
        return temp * temp % 1000000007
    else:
        temp = square(a, b-1)
        return temp * a % 1000000007
    
# 페르마의 소정리 이용해서 해당 문제를 해결할 수 있다.
# nCk​ % P = n! x ((n−k)!k!)^P−2 % P 
# 처음 알았음
top = fact(n)
bottom = fact(n-k) * fact(k) % 1000000007

print(top * square(bottom, 1000000005) % 1000000007)


