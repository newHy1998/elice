import operator

n = int(input())
p_list = list(map(int, input().split(" ")))
p_dict = dict(enumerate(p_list))
cost_time = 0
p_dict = dict(sorted(p_dict.items(), key = operator.itemgetter(1)))

cur = 0
i = 0

for k, b in p_dict.items():
    
    if i >= 1:
        cost_time += cur
        
    cost_time += b
    cur += b
    i += 1
    
print(cost_time)