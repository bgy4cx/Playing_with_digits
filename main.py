def dig_pow(n, p):
    k = 0
    for i in range(len(str(n))):
        k += pow(int(str(n)[i]), (p + i) )
    return k / n if k % n == 0 else -1