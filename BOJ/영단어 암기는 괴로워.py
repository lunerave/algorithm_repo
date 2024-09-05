from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict(list)

for _ in range(n):
    word = input()
    if len(word) < m:
        continue

    if word not in dic:
        dic[word].append([1, len(word), word])
    else:
        dic[word][0][0] += 1
    

word_list = []

for v in dic.values():
    word_list.append(v[0])


word_list.sort(key=lambda x:(-x[0], -x[1], x[2]))

for w in word_list:
    print(w[2])


