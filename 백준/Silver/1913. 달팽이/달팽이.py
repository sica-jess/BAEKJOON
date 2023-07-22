# direction = [[1,0],[0,1],[-1,0], [0,-1]]
# curr_y = 0
# curr_x = 0
# curr_dir = 0 # 0 down, 1 right, 2 up, 3 left
# for i in range(4):
#     curr_dir = i
#     next_y = curr_y + direction[curr_dir][0]
#     next_x = curr_x + direction[curr_dir][1]
#     print(next_y, next_x)


# n = int(input())
# direction = [[1,0],[0,1],[-1,0], [0,-1]]
# curr_y = 0
# curr_x = 0
# curr_dir = 0 # 0 down, 1 right, 2 up, 3 left
# for i in range(n):
#     curr_dir = i
#     next_y = curr_y + direction[curr_dir][0]
#     next_x = curr_x + direction[curr_dir][1]
#
#     print(curr_y, curr_x,
#     direction[curr_dir][0],direction[curr_dir][1],
#     next_y, next_x)


n = int(input())
number = int(input())
direction = [[1,0],[0,1],[-1,0], [0,-1]]

snail = [[0 for _ in range(n)] for _ in range(n)]

start = n * n
curr_y = 0
curr_x = 0
curr_dir = 0 # 0 down, 1 right, 2 up, 3 left
solution = list()

for _ in range(n * n):
    if start == number:
        solution.append(curr_y + 1)
        solution.append(curr_x + 1)

    snail[curr_y][curr_x] = start
    next_y = curr_y + direction[curr_dir][0]
    next_x = curr_x + direction[curr_dir][1]
    if next_y < 0 or next_x < 0 or next_y >= n or next_x >= n or snail[next_y][next_x] != 0:
        curr_dir += 1
        curr_dir %= 4 # 0, 1, 2, 3

    curr_y = curr_y + direction[curr_dir][0]
    curr_x = curr_x + direction[curr_dir][1]
    start -= 1

for y in range(n):
    for x in range(n):
        print(snail[y][x], end=' ')
    print()
print(solution[0], solution[1]) #좌표값 출력