import heapq
import sys
heap = []

n = int(input())
ans_list = []

for i in range(n):
    m = int(sys.stdin.readline())
    
    if m == 0:
        if len(heap) == 0:
            ans_list.append(0)
            continue
            
        ans_list.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, (m))
        
for ans in ans_list:
    print(ans)