import random

def nospace(xx):
    s = ""
    for x in xx: s = s + str(x)
    return s

def split(vec):
    l = len(vec)//2
    return vec[:l], vec[l:]

def merge(aa,bb):
    res = []
    for a in aa: res.append(a)
    for b in bb: res.append(b)
    return res

def xor(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]^b[i])
    return c

def select(source, selection):
    result = []
    for index in selection:
        result.append(source[index-1])
    return result

def LS(xx):
    yy = []
    for x in xx[1:]:
        yy.append(x)
    yy.append(xx[0])
    return yy

def toBinArray(x,len):
    s = []
    b = 1<<(len-1)
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
     
def toHex(x):
    return hex(x)[2:]

def toUpper(c):
    if(c >= 'a' and c <= 'z'): return chr(ord(c) - 32)
    return c

def prettyHex(x,l):
    h = toHex(x)
    hh = ""
    for i in h: hh = hh + toUpper(i)

    for i in range(l - len(hh)): hh = "0" + hh

    return hh

def prepareDes(s):
    l = len(s)
    ll = ((l-1)//8 + 1)*8

    for j in range(ll - l): s = s + " "

    result = []
    part = []

    for i in range(ll):
        
        if i%8 == 0 and i > 0:
            result.append(part)
            part = []

        xbin = toBinArray(ord(s[i]),8)

        for x in xbin:
            part.append(x)

    result.append(part)

    return result 

def randomDesKey():
    key = []

    for i in range(8):
        par = 0
        for j in range(7):
            r = random.randrange(0,2)
            par = par^r
            key.append(r)

        key.append(par)

    return key

def randByte():
    return random.randrange(0,1<<12)

def getKey(byte):
    #keytext = byte*(1 + (1<<9) + (1<<19)) + (255-byte)*((1<<25) + (1<<33) + (1<<49))
    keytext = byte**3 + byte**2 + 0x1212*byte
    return toBinArray(keytext,64)

