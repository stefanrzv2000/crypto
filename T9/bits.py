def b_xor(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]^b[i])
    return c

def b_add(a,b):
    c = toInt(a) + toInt(b)
    return toBinArray(c,len(a))

def b_or(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]|b[i])
    return c

def b_and(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]&b[i])
    return c

def b_not(a):
    c = []
    for i in range(len(a)):
        c.append(1-a[i])
    return c

def hamming(a,b):
    c = 0
    for i in range(len(a)):
        c = c + a[i]^b[i]
    return c

def LS(xx, l = 1):
    yy = []
    for x in xx[l:]:
        yy.append(x)
    for x in xx[:l]:
        yy.append(x)
    return yy

def toBinArray(x,lenn):
    s = []
    b = 1<<lenn
    x = x%b
    b = b>>1
    while(b > 0):
        if(x>=b): s.append(1); x = x-b
        else: s.append(0)
        b = b>>1
    return s

def toInt(B):
    x = 0

    for b in B:
        x *= 2
        if b: x += 1

    return x