import random

def RC4Init(key):
    l = len(key)
    j = 0
    S0 = []
    for i in range(256): S0.append(i)

    for i in range(256):
        j = (j + S0[i] + key[i%l])%256
        aux = S0[i]
        S0[i] = S0[j]
        S0[j] = aux
    
    return 0,0,S0

def RC4Trans(i,j,S):
    i = (i + 1)%256
    j = (j + S[i])%256
    
    aux = S[i]
    S[i] = S[j]
    S[j] = aux

    byte = S[(S[i]+S[j])%256]

    return byte, i, j, S

def RC4keystream(key, length):
    i,j,S = RC4Init(key)

    keystream = []

    for index in range(length):
        byte, i, j, S = RC4Trans(i,j,S)
        keystream.append(byte)

    return keystream

def toIntArray(s):
    rez = []
    for c in s:
        rez.append(int(ord(c)))

    return rez

def toString(a):
    s = ""
    for c in a:
        s = s + chr(c)
    return s

def randomKey(leng):
    key = []
    for i in range(leng):
        key.append(random.randrange(256))
    return key

def enc(message,key):
    keystream = RC4keystream(key,len(message))
    s = []
    for i in range(len(message)):
        s.append(ord(message[i])^keystream[i])
    
    return s

def toHex(a):
    s = ""
    for x in a:
        s = s + hex(x)[2:] + " "
    return s
#key = toIntArray("AnaAreMere")

#print(toIntArray("blabla"))

#"""
key = toIntArray("anaaremere")

key = [0x80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x = RC4keystream(key,64)

print(x)

print(toHex(x))

#print(toString(x))

print(key)

message = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqazx bgrewsxc bnhygv mjhgv mkjuygfv mkjhgfdertgb mkjhbvcdrtgb utdhgv"

x = enc(message,key)

print(enc(message,key))

print(chr(97))

#print(toString([87,245]))



#print(RC4keystream(key,200))
#"""

#"""
#experiment
"""
max = 10
cases = 2**18
zeros = []
keylen = 16
for i in range(max): zeros.append(0)

for i in range(cases):
    keystream = RC4keystream(randomKey(keylen),max)
    for j in range(max):
        if(keystream[j] == 0): zeros[j] += 1

p = []

for i in range(max):
    p.append(zeros[i]/cases*256)

for i in range(max):
    print("P(Z" + str(i+1) + " = 0) = " + str(p[i]) + "/256")
"""
