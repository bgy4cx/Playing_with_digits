def dig_pow(n, p):
    k = 0
    for i in range(len(str(n))):
        k += pow(int(str(n)[i]), (p + i) )
    if k % n == 0:
        k = k / n
    else:
        k = -1      
    return k