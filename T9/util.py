import random
import struct
from bits import *

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

def readBytes(file):
    fin = open(file, "rb")
    fileContents = fin.read()
    fin.close()
    return bytearray(fileContents)

def writeBytes(B, file):
    fout = open(file,"wb")
    fout.write(B)

def preprocess(B):

    Bc = []
    for b in B: Bc.append(b)

    ml = len(Bc)*8 & 0xffffffffffffffff
    mlb = ml.to_bytes(8,byteorder = 'big')

    Bc.append(0x80)
    
    to_add = (120 - len(Bc)%64)%64

    for i in range(to_add): Bc.append(0)

    for b in mlb: Bc.append(b)

    return Bc

    #print("new len = " + str(len(B)))

def chunks(B,size = 64):
    chunks = []
    l = len(B)

    for i in range(0,l,size):
        chunks.append(B[i:i+size])

    return chunks

def chunkToBinArray(chunk):
    rez = []
    for x in chunk:
        for b in toBinArray(x,8):
            rez.append(b)

    return rez

def splitChunk(chunk):
    wchs = chunks(chunk,4)
    w = []
    for wch in wchs: w.append(chunkToBinArray(wch))
    return w

def takeStep(a,b,c,d,e,f,k,w):
    temp = toInt(LS(a,5)) + toInt(f) + toInt(e) + toInt(k) + toInt(w)
    temp = toBinArray(temp,32)
    e = d
    d = c
    c = LS(b,30)
    b = a
    a = temp

    """
    print("\ta = " + prettyHex(toInt(a),8))
    print("\tb = " + prettyHex(toInt(b),8))
    print("\tc = " + prettyHex(toInt(c),8))
    print("\td = " + prettyHex(toInt(d),8))
    print("\te = " + prettyHex(toInt(e),8))
    print("")
    """

    return a,b,c,d,e


def randByte(x = 8):
    return random.randrange(0,1<<x)

def genSelection(seed, index = 0):

    if(seed < 0): return []

    seed = (seed<<30) + ((3*seed+15)<<15) + (11*seed)
    #print (prettyHex(seed,20))
    selection = []
    for j in toBinArray(seed,50):
        if j > 0: selection.append(index)
        index = index+1
    
    return selection

def mutate(source, selection):
    rez = bytearray()

    for s in source: rez.append(s)

    for j in selection:
        rez[j] = rez[j]^1
    
    return rez

def first32(barray, length = 8):
    return prettyHex(toInt(barray),(len(barray)+3)//4)[:length]

def afisare_dict(d):
    for k in d:
        print(str(k) + " : " + str(d[k]))

def afisare_dicts(d1,d2):
    s = []

    for k1, k2 in d1, d2:
        s.append(str(k1) + " : " + str(d1[k1]) + " \t-\t " + str(k2) + " : " + str(d2[k2]))

    for ss in s: print(s)

def print_keys(d):
    s = ""
    for k in d: s = s + str(k) + " " 
    print(s)