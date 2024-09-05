temp = []

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    t = max(a, b, c)

    if sum([a, b, c]) - t <= t:
        temp.append("Invalid")
        continue

    s = set([a, b, c])

    if len(s) == 3:
        temp.append("Scalene")
    elif len(s) == 2:
        temp.append("Isosceles")
    else:
        temp.append("Equilateral")
    
for i in range(len(temp)):
    print(temp[i])
    


