h, w = map(int, input().split())

blocks = list(map(int, input().split()))

answer = 0

for i in range(1, w-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])

    target = min(left, right)

    if blocks[i] < target:
        answer += target - blocks[i]

print(answer)

    


