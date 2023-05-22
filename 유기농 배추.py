from sys import stdin
import sys
sys.setrecursionlimit(99999)
test_num = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
worm_num_list = []

def dfs(x, y):
    global x_size
    global y_size
    visited[x][y] = 1
    
    for d in range(4):
        mx = x + dx[d]
        my = y + dy[d]
        
        if 0 <= mx < y_size and 0 <= my < x_size:
            if matrix[mx][my] == 1 and visited[mx][my] == 0:
                dfs(mx, my)
    
for i in range(test_num):
    y_size, x_size, cab_num = list(map(int, input().split(" ")))
    matrix = [[0] * x_size for i in range(y_size)]
    visited = [[0] * x_size for i in range(y_size)]
    worm_num = 0
        
    for j in range(cab_num):
        c_x, c_y = list(map(int, stdin.readline().strip().split(" ")))
        matrix[c_x][c_y] = 1

    for a in range(y_size):
        for b in range(x_size):
            if matrix[a][b] == 1 and visited[a][b] == 0:
                dfs(a, b)
                worm_num += 1
                
    worm_num_list.append(worm_num)


for worm_num in worm_num_list:
        print(worm_num)
    
    