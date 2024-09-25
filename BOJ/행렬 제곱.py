n, b = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

# 행렬 곱셈 구현
def multi(a, b):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][k] += (a[i][j] * b[j][k]) % 1000 

    return temp

# 분할정복을 통한 거듭제곱 구현
def square(x, n):
    if n == 1:
        return x

    # 짝수 일 경우, n^2 = n^1 * n^1
    if n % 2 == 0:
        temp = square(x, n//2)
        return multi(temp, temp)
    else: # 홀수 일 경우, n^3 = n^2 * n^1
        temp = square(x, n-1)
        return multi(x, temp)

result = square(maps, b)

# 문제 조건 충족을 위한 추가 연산
for i in range(n):
    for j in range(n):
        result[i][j] = result[i][j] % 1000

# *를 사용하면 리스트 내의 값이 한번에 출력됨. 처음 알았음
for k in result:
    print(*k)



