n, play = input().split()

n = int(n)

answer = 0

if play == 'Y':
    people_need = 1
elif play == 'F':
    people_need = 2
elif play == 'O':
    people_need = 3

played = set()

people_count = 0

for _ in range(n):
    people = input()
    if people in played:
        continue

    played.add(people)
    people_count += 1

    if people_count == people_need:
        answer += 1
        people_count = 0

print(answer)