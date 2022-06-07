def dig_pow(n, p):
    k=0
    for i in range(len(str(n))):
        k += f_computing(int(str(n)[i]), p)
        p += 1
    if k % n != 0:
        k = -1
    else:
        k = k / n 
        
    return k

def f_computing(digit, p):
    return pow(digit, p)