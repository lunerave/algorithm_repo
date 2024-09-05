string = input()

string = string.upper()

dic = {}

for s in string:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

temp = sorted(dic.items(), key = lambda x: -x[1])

if len(temp) == 1:
    print(temp[0][0])
else:    
    if temp[0][1] == temp[1][1]:
        print("?")
    else:
        print(temp[0][0])

