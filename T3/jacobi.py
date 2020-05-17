from random import randrange, getrandbits
import os

def is_prime(n, k=128):
    """ 
    Test if a number is prime        
    Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False    
    return True

def generate_prime_candidate(length):
    """ 
    Generate an odd integer randomly        
    Args:
            length -- int -- the length of the number to generate, in bits        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 3   
    return p

def generate_prime_number(length=1024):
    """ 
    Generate a prime        
    Args:
            length -- int -- length of the prime to generate, in          bits        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128) or p%4!=3:
        p = generate_prime_candidate(length)
    return p
    
#print(generate_prime_number())

def Jacobi(a,n):
    b = a%n
    c = n
    s = 1
    while(b>=2):
        while(b%4==0): b=b/4
        if(b%2 == 0):
            if(c%8 == 3 or c%8 == 5): s=-s
            b = b/2
        if(b==1): break
        if(b%4 == 3 and c%4 == 3):
            s = -s
        aux = b
        b = c % b
        c = aux
    return s*b

def print_bin(x):
    """
    transforms x (some jacobi symbol) to 0 or 1
    """
    if(x == -1): return("0")
    if(x == 1): return("1")
    return ""

n = generate_prime_number(512)*generate_prime_number(512)

print("gata")

s = ""

a = randrange(0,n,1)

k = 2**16


for i in range(k):
    #print("(" + str(a) + "/" + str(n) + ") = " + str(Jacobi(a,n)))
    s = s + print_bin(Jacobi(a+i,n))

f = open("jacobi.txt","w")
f.write(s)

f.close()

os.system('python3 test.py jacobi.txt')