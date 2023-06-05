x = 600851475143
m = 2

while x != 1:
    remaider = x%m
    if remaider == 0:
        x = x/m
        print(m)
    else:
        m +=1    
