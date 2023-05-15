from collections import deque

program_strs = list(map(int, input().split(" ")))
v_num = program_strs[0]
e_num = program_strs[1]
start_v = program_strs[2]
e = {}

def recursion_dfs(start_v, discovered = []):
    discovered.append(start_v)
    for w in e[start_v]:
        if w not in discovered:
            discovered = recursion_dfs(w, discovered)
    return discovered
    
def bfs(start_v, e):
    bfs_discoverd = [start_v]
    queue = deque()
    queue.append(start_v)
    
    while queue:
        pop_v = queue.popleft()
        for w in e[pop_v]:
            if w not in bfs_discoverd:
                bfs_discoverd.append(w)
                queue.append(w)
                
    return bfs_discoverd
    
for i in range(v_num + 1):
    e[i] = []
    
for i in range(e_num):
    program_strs = list(map(int, input().split(" ")))
    e[program_strs[0]].append(program_strs[1])
    e[program_strs[1]].append(program_strs[0])
    e[program_strs[0]].sort()
    e[program_strs[1]].sort()

dfs_discovered = recursion_dfs(start_v, [])
bfs_discovered = bfs(start_v, e)

for i in dfs_discovered:
    print(i, end = " ")
    
print()

for i in bfs_discovered:
    print(i, end = " ")
    
print()