value_len = int(input())
value_list = []

for i in range(value_len):
    value = int(input())
    
    if value == 0:
        value_list.pop()
        continue
        
    value_list.append(value)
    
print(sum(value_list))