n, k, p, x = map(int, input().split())

# 0을 추가해서 자릿수를 맞춰준다
x = str(x).rjust(k, '0')

answer = 0

# 각 숫자에 대한 딕셔너리 저장 1은 켜져있음, 0은 꺼져있음
dic = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1010010',
    '8' : '1111111',
    '9' : '1111011'
}

# 현재 층수에 대한 딕셔너리 값 저장
current_floor = [dic[num] for num in x]

# 1층부터 n층까지 주어진 p 내에서 변환가능 확인
for i in range(1, n+1):
    destination = str(i).rjust(k, '0')
    destination_floor = [dic[num] for num in destination]

    diff = 0

    for cur, des in zip(current_floor, destination_floor):
        for c, d in zip(cur, des):
            if c != d:
                diff += 1
        
        if diff > p:
            break
    
    if diff <= p and diff > 0:
        answer += 1

print(answer)
        


