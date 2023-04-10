n, m = list(map(int, input().split(" ")))
s = []
discovered = []

def tracking():
    if n == m:
        for i in range(1, n + 1):
            print(i, end = " ")
        print()
        return
    
    if len(s) == m:
        sub_s = sorted(s)
        combine = " ".join(list(map(str, sub_s)))
        if combine not in discovered:
            discovered.append(combine)
            print(" ".join(list(map(str, s))))
            
        return
    
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            tracking()
            s.pop()
            
tracking()