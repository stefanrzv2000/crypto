from util import *
from sys import stdout 


def sha1(BB, verbose = False):

    h0 = toBinArray(0x67452301,32)
    h1 = toBinArray(0xEFCDAB89,32)
    h2 = toBinArray(0x98BADCFE,32)
    h3 = toBinArray(0x10325476,32)
    h4 = toBinArray(0xC3D2E1F0,32)    

    B = preprocess(BB)

    if(verbose): print(len(B))

    ii = 1

    for chunk in chunks(B):
    
        """
        print("chunck " + str(ii))
        ii = ii+1

        print(chunk)

        print(nospace(h0))
        print(nospace(h1))
        print(nospace(h2))
        print(nospace(h3))
        print(nospace(h4))
        print(" ")
        """

        w = splitChunk(chunk)

        for i in range(16,80,1):
            w.append(LS(
                b_xor(
                    b_xor(w[i-3],w[i-8]),
                    b_xor(w[i-14],w[i-16])
                    )
                )
            )

        index = 0
        if(verbose):
            for ww in w: 
                print(str(index) + " " + prettyHex(toInt(ww),8))
                print(str(index) + " " + nospace(ww))
                index = index + 1
        
        #print(len(w))

        ha = h0
        hb = h1
        hc = h2
        hd = h3
        he = h4

        f = []

        for jj in range(0,20,1):
            f = b_or(
                b_and(hb,hc),
                b_and(b_not(hb),hd)
            )
            k = toBinArray(0x5A827999,32)
            
            #print(jj)
            ha,hb,hc,hd,he = takeStep(ha,hb,hc,hd,he,f,k,w[jj])

        for jj in range(20,40,1):
            f = b_xor(
                b_xor(hb,hc),
                hd
            )
            k = toBinArray(0x6ED9EBA1,32)
            
            #print(jj)
            ha,hb,hc,hd,he = takeStep(ha,hb,hc,hd,he,f,k,w[jj])

        for jj in range(40,60,1):
            f = b_or(
                b_or(
                    b_and(hb,hc),
                    b_and(hb,hd)
                ),
                b_and(hc,hd)
            )
            k = toBinArray(0x8F1BBCDC,32)
            
            #print(jj)
            ha,hb,hc,hd,he = takeStep(ha,hb,hc,hd,he,f,k,w[jj])

        for jj in range(60,80,1):
            f = b_xor(
                b_xor(hb,hc),
                hd
            )
            k = toBinArray(0xCA62C1D6,32)
            
            #print(jj)
            ha,hb,hc,hd,he = takeStep(ha,hb,hc,hd,he,f,k,w[jj])


        h0 = b_add(h0,ha)
        h1 = b_add(h1,hb)
        h2 = b_add(h2,hc)
        h3 = b_add(h3,hd)
        h4 = b_add(h4,he)

    hh = []

    for h in h0: hh.append(h)
    for h in h1: hh.append(h)
    for h in h2: hh.append(h)
    for h in h3: hh.append(h)
    for h in h4: hh.append(h)

    return hh

def attackBytes(barray1,barray2, length = 8, index = 0):

    #print("")
    #print(len(barray1))
    #print(len(barray2))

    sha11 = sha1(barray1, verbose=False)
    sha12 = sha1(barray2, verbose=False)

    #print("sha1_1   = " + prettyHex(toInt(sha11),20))
    #print("sha1_2   = " + prettyHex(toInt(sha12),20))

    f1 = first32(sha11,length)
    f2 = first32(sha12,length)

    #print(first32(sha11))
    #print(first32(sha12))

    d1 = dict()
    d2 = dict()

    d1[f1] = -1
    d2[f2] = -1

    s1 = 0
    s2 = 0

    for i in range(1<<32):
        
        seed = random.randrange(1<<20)
        #seed = i

        selection = genSelection(seed,index)
        f1 = first32(sha1(mutate(barray1,selection)),length)
        f2 = first32(sha1(mutate(barray2,selection)),length)

        #print(f1,f2)

        #print(barray1)

        d1[f1] = seed
        d2[f2] = seed

        if(i%100 == 0 and i!=0): 
            print(".",end = "")
            stdout.flush()
            #print(f1,f2)

        if f1 in d2:

            s1 = d1[f1]
            s2 = d2[f1]
            break

        if f2 in d1:
            #print(f2)
            s2 = seed
            s1 = d1[f2]
            break


    nba1 = mutate(barray1,genSelection(s1,index))
    nba2 = mutate(barray2,genSelection(s2,index))

    #print(len(nba1))
    #print(len(nba2))
    print("")

    return nba1, nba2

def attackFiles(file1, file2, length):

    print("\nprocessing images...", end = "")

    barray1 = readBytes(file1)
    barray2 = readBytes(file2)

    nba1, nba2 = attackBytes(barray1,barray2, length, 100)

    nfile1 = "new_" + file1
    nfile2 = "new_" + file2

    writeBytes(nba1,nfile1)
    writeBytes(nba2,nfile2)



x = []

for j in range(534): x.append(randByte())

text1 = "abc"
text2 = "acc" #one bit changed: b = 01100010, c = 01100011
bt1 = bytearray()
bt1.extend(map(ord, text1))
bt2 = bytearray()
bt2.extend(map(ord, text2))

sha11 = sha1(bt1)
sha12 = sha1(bt2)

print("text1 = " + text1)
print("sha1_1 = " + nospace(sha11))
print("sha1_2 = " + nospace(sha12))
print("sha1_1   = " + prettyHex(toInt(sha11),20))
print("expected = " + "A9993E364706816ABA3E25717850C26C9CD0D89D")

print("sha1_2   = " + prettyHex(toInt(sha12),20))
print("hamming distance = " + str(hamming(sha11,sha12)))
print("______________________________________________________\n")

#"""
attackFiles("battleship.bmp", "mac.bmp",4)
bt1 = readBytes("new_battleship.bmp")
bt2 = readBytes("new_mac.bmp")

sha11 = sha1(bt1)
sha12 = sha1(bt2)

print("sha1_battleship = " + prettyHex(toInt(sha11),20))
print("sha1_flower     = " + prettyHex(toInt(sha12),20))
#"""

#"""
text1 = "qazwsxedcrfvtgbyhnujmik,ol.p;/['][poiuytrewqasdfghj"
text2 = "bchdkahdnsmxboenskckqlsjba,mbsiudqweqweqweqaqasdsdf"

bt1 = bytearray()
bt1.extend(map(ord, text1))
bt2 = bytearray()
bt2.extend(map(ord, text2))

print("___________________________________________________\n")
print("processing texts...", end = "")
nba1, nba2 = attackBytes(bt1, bt2,4)

text1 = nba1.decode("utf-8")
text2 = nba2.decode("utf-8")

print("")
print("text1_m = " + text1)
print("text2_m = " + text2)
print("")

bt1 = bytearray()
bt1.extend(map(ord, text1))
bt2 = bytearray()
bt2.extend(map(ord, text2))

sha11 = sha1(bt1)
sha12 = sha1(bt2)

print("sha1_1m = " + prettyHex(toInt(sha11),20))
print("sha1_1m = " + prettyHex(toInt(sha12),20))
#"""

text1 = "pa{wsyddbrgvtfbyioujmhj-nm/p;/Z&\Zpoiuxusevqareffhj"
text2 = "bbidkaiensmxcodnskckqlrjb`,mbsitdqweqvepwdq`qardsef"

print("")
print("text1_m = " + text1)
print("text2_m = " + text2)
print("")

bt1 = bytearray()
bt1.extend(map(ord, text1))
bt2 = bytearray()
bt2.extend(map(ord, text2))

sha11 = sha1(bt1)
sha12 = sha1(bt2)

print("sha1_1m = " + prettyHex(toInt(sha11),20))
print("sha1_1m = " + prettyHex(toInt(sha12),20))