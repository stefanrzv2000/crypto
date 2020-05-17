import random

def delta(state,key):
    result = 0
    for i in range(len(state)):
        result = (result+(state[i]*key[i]))%2
    return result

def LFSRtransition(state,key):
    out = state[0]

    for i in range(len(state)-1):
        state[i] = state[i+1]
    
    state[i+1] = delta(state,key)

    return out

def tostr(state):
    s = ""
    for c in state:
        s = s + str(c)
    return s

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

def findPeriod(state,key):
    states = {tostr(state) : 1}
    
    while(len(states) < 1000000):
        LFSRtransition(state,key)
        #print("state = " + tostr(s))

        if(tostr(state) in states): return (len(states) + 1,states[tostr(state)])
        states[tostr(state)] = len(states) + 1

    return (0,0)

def randomsk(keylength):
    key = []
    for i in range(keylength):  key.append(random.randrange(2))

    state = []
    for i in range(keylength): state.append(random.randrange(2))

    return (state,key)

s,k = randomsk(20)

print("key   = " + tostr(k))
print("")
print("state = " + tostr(s))

x,y = findPeriod(s,k)

print(x,y,x-y)

"""
f = open("LFSR.txt","w")
f.write(LFSRgenerate(2**16))
"""