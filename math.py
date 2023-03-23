res_list = []

while True:
    n, m = map(int, input().split(" "))
    if n == 0 and m == 0:
        break
    if m % n == 0:
        res_list.append("factor")
        continue
    elif n % m == 0:
        res_list.append("multiple")
        continue
    else:
        res_list.append("neither")
        continue
    
for res in res_list:
    print(res)