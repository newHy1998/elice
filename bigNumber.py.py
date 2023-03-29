large = int(input())
val_list = input().split(" ")
val_list = list(map(int, val_list))
stack_list = []
res = [-1 for i in range(large)]

for i in range(large):
    if not stack_list:
        stack_list.append(i)
        continue
        
    while stack_list and val_list[i] > val_list[stack_list[-1]]:
        index = stack_list.pop()
        res[index] = val_list[i]

    stack_list.append(i)
    
for i in res:
    print(i, end = ' ')