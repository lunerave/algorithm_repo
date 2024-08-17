n = int(input())

words = []

for _ in range(n):
    words.append(input())

# 사전순으로 정렬하여, 접두사 탐색을 효율적으로 바꿈
# 인덱스를 같이 저장하여, 이후 출력에 활용
sorted_words = sorted(enumerate(words), key = lambda x:x[1])

# 두 문자열의 같은 접두사 탐색
def check(a, b):
    min_len = min(len(a), len(b))
    count = 0
    for i in range(min_len):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count

# 각 문자의 접두사 길이 저장
length = [0] * n

# 입력 받은 문자열 중 가장 긴 접두사 길이
max_length = 0

for i in range(n-1):
    tmp = check(sorted_words[i][1], sorted_words[i+1][1])
    max_length = max(max_length, tmp)

    # 각 문자의 접두사 최대 길이 저장
    length[sorted_words[i][0]] = max(length[sorted_words[i][0]], tmp)
    length[sorted_words[i+1][0]] = max(length[sorted_words[i+1][0]], tmp)

# 첫 번째 단어를 찾았는 지를 알기 위한 flag
first_flag = 0

for i in range(n):
    if first_flag == 0:
        if length[i] == max_length:
            first_flag = 1
            print(words[i])
            # 접두사를 저장해서, 같은 max_length를 가졌더라도 문제의 조건에 맞는 문자 출력
            prefix = words[i][:max_length]
    else:
        if length[i] == max_length and words[i][:max_length] == prefix:
            print(words[i])
            break

