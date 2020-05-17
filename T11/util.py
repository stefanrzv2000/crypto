from random import randrange
from primes import *


def euclid(a,b,x = 0):
    
    x = x+1
    #print(x)

    if a == 0: return 0, 1, b
    if b == 0: return 1, 0, a

    if(a < b):
        u0,v0,d0 = euclid(b,a,x)
        return v0,u0,d0

    r = a%b
    c = a//b
    u0,v0,d0 = euclid(b,r,x)

    """
    a = bc + r
    r = a - bc

    d = ub + vr
    d = ub + va - vbc
    d = va + (u-vc)b

    """

    return v0,(u0-v0*c),d0

def inverse(x, mod):
    u,v,d = euclid(x,mod)
    if(d!=1): return 0
    return u%mod

def TCR(residues, modules):
    cc = 1
    c = []
    x = 0
    for m in modules: cc = cc*m
    for m in modules: c.append((cc//m))

    for i in range(len(modules)):
        inv = inverse(c[i],modules[i])
        xi = (residues[i]*inv)%modules[i]
        x = (x + xi*c[i])%cc

    return x
    
def gen_rsa(l = 512):
    p = generate_prime_number(l)
    q = p
    while(p==q): q = generate_prime_number(l)

    n = p*q
    phi=(p-1)*(q-1)

    d = 0
    e = 0
    while(d**4 < n): 
        e = randrange(l,l*l)
        d = inverse(e,phi)

    return n,p,q,e,d

def gen_rsa_wien(l = 512):
    p = generate_prime_number(l)
    q = p
    while(p==q): q = generate_prime_number(l)

    n = p*q
    phi=(p-1)*(q-1)

    d = 0
    e = 0
    while(e < 1): 
        d = randrange(1<<254)
        e = inverse(d,phi)

    if(p < q and q < 2*p): return n,p,q,e,d
    elif(q < p and p < 2*q): return n,p,q,e,d
    else: return gen_rsa_wien(l)

def mod_pow_TCR(base,exp,p,q):
    x1 = pow(base%p,exp%(p-1),p)
    x2 = pow(base%q,exp%(q-1),q)

    return TCR([x1,x2],[p,q])

def bytes_to_int(bytess):
    x = 0
    for b in bytess:
        x<<=8
        x+=b
    
    return x

def int_to_bytes(x,l):
    s = []
    b = 1<<(l*8)
    x = x%b
    b = b>>8
    while(b > 0):
        r = x//b
        x = x-r*b
        s.append(r)
        b = b>>8
    return s

def string_to_int(text):
    bt1 = bytearray()
    bt1.extend(map(ord, text))
    return bytes_to_int(bt1)

def int_to_string(x):
    l = (int.bit_length(x)-1)//8 + 1
    bb = int_to_bytes(x,l)
    s = ""

    for b in bb: s = s + chr(b)
    return s


# xx = string_to_int("abcdabc")
# print(xx)
# print(int_to_string(xx))
