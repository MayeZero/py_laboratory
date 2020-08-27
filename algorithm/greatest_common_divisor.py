def gcd(a,b):
    if b == 0:
        print(a)
    else:
        if a > b:
            tmp = b
            b = a % b
            a = tmp
        else:
            b = b % a
        gcd(a,b)
    return None
    
