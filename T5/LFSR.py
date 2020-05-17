import random
import sys
import os

def delta(state,key):
    result = 0
    for i in range(len(state)):
        result = (result+(state[i]*key[i]))%2
    return result

def LFSRtransition(state,key):
    out = state[0]

    for i in range(len(state)-1):
        state[i] = state[i+1]
    
    state[i] = delta(state,key)

    return out

def LFSRgenerate(nrBits, keylength = 32, key = 0):
    s = ""
    if key!=0: keylength = len(key)
    else :
        key = []
        for i in range(keylength):  key.append(random.randrange(2))
        
    state = []
    for i in range(keylength): state.append(random.randrange(2))
    
    for i in range(2*keylength): LFSRtransition(state,key)

    for i in range(nrBits): s = s + str(LFSRtransition(state,key))

    return s

def randomsk(keylength):
    key = []
    for i in range(keylength):  key.append(random.randrange(2))

    key[0] = 1

    state = []
    for i in range(keylength): state.append(random.randrange(2))

    return (state,key)

def LFSRgen(nrBits,key,state):
    s = ""
    keylength = len(key)
    for i in range(2*keylength): LFSRtransition(state,key)

    for i in range(nrBits): s = s + str(LFSRtransition(state,key))

    return s

def tostr(state):
    s = ""
    for c in state:
        s = s + str(c)
    return s

def findPeriod(state,key):
    states = {tostr(state) : 1}

    ff = open("LFSRstates.txt",'w')
    
    while(len(states) < 1000000):
        LFSRtransition(state,key)
        ff.write("state = " + tostr(s) + "\n")

        if(tostr(state) in states): return (len(states) + 1,states[tostr(state)])
        states[tostr(state)] = len(states) + 1

    ff.close()

    return (0,0)

f = open("LFSR.txt","w")

length = 16

if(len(sys.argv) > 1): length = int(sys.argv[1])

s,k = randomsk(length)

print("key   = " + tostr(k))
print("")
print("state = " + tostr(s))

x,y = findPeriod(s,k)

print("")
print("period = " + str(x-y))
print("")

f.write(LFSRgen(2**16,k,s))

f.close()

os.system('python3 test.py LFSR.txt')