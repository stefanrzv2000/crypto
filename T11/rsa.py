from primes import *
from util import *
import time

def enc(x,n,e):
    return pow(x,e,n)

def dec(x,n,d):
    return pow(x,d,n)

def dec_TCR(x,p,q,d):
    return mod_pow_TCR(x,d,p,q)

n,p,q,e,d = gen_rsa()

text = "abcdbcdecdefdefg"

xx = string_to_int(text)
print("xx  = " + str(xx))

crixx = enc(xx,n,e)

print("cri = " + str(crixx))

decxx = dec(crixx,n,d)

print("dec = " + str(decxx))

print("dec_text = " + int_to_string(decxx))

print("\n\n\nstarting testing\n")

t_start = time.time()

for i in range(1000):
    decxx = dec(crixx,n,d)

t_end = time.time()

print("no TCR : " + str(t_end - t_start) + " seconds")

t_start = time.time()

for i in range(1000):
    decxx = dec_TCR(crixx,p,q,d)

t_end = time.time()

print("   TCR : " + str(t_end - t_start) + " seconds")