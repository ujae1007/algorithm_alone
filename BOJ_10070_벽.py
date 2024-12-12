N, K = list(map(int, input().split()))
task = [list(map(int, input().split())) for _ in range(K)]

blocks = [0] * N

for op, left, right, height in task:
    for i in range(left, right+1, 1):
        if op == 1:
            if blocks[i] < height:
                blocks[i] = height
        else:
            if blocks[i] > height:
                blocks[i] = height

for num in blocks:
    print(num)
