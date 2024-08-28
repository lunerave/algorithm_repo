a, b = map(int, input().split())
psum = [0] * 60

# 점화식을 통해서 각 2**i-1까지 등장하는 1의 개수 저장
for i in range(1, 60):
    psum[i] = 2**(i-1) + 2*psum[i-1]

# a 이전까지 1의 개수 카운트
count_a = 0
a -= 1
bin_a = bin(a)[2:]

for i in range(len(bin_a)):
    if bin_a[i] == '1':
        # a보다 크지 않으면서 가장 큰 2의 거듭제곱 수
        pow = len(bin_a) - i - 1
        # a 보다 작은 자리수를 가지는 수의 1을 모두 카운트한 수 저장
        count_a += psum[pow]
        # 현재 숫자의 가장 앞자리 1 개수 저장
        count_a += a - 2**pow + 1
        a = a - 2**pow

count_b = 0
bin_b = bin(b)[2:]

for i in range(len(bin_b)):
    if bin_b[i] == '1':
        pow = len(bin_b) - i - 1
        count_b += psum[pow]
        count_b += b - 2**pow + 1
        b = b - 2**pow

print(count_b-count_a)
