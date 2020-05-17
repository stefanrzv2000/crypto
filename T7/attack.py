from des import *
from util import *

"""
criptare + decriptare
"""

plaintext   = 0x0123456789abcdef
plainArray  = toBinArray(plaintext,64)

keytext     = 0x133457799bbcdff1
keyArray    = toBinArray(keytext,64)

cryptoArray = encrypt(plainArray,keyArray)
cryptotext  = toInt(cryptoArray)

decArray    = decrypt(cryptoArray,keyArray)
dectext     = toInt(decArray)

print("cry: " + prettyHex(cryptotext,16))
print("dec: " + prettyHex(dectext,16))


"""
ATTACK
"""

key1 = getKey(randByte())
key2 = getKey(randByte())

print("\n\nATTACK:\n")

print("init_key1: " + prettyHex(toInt(key1),16))
print("init_key2: " + prettyHex(toInt(key2),16))
print("")

text = "Ana are mere si pere 12345"

plains = prepareDes(text)

cryptos = []

for p in plains: 
    c = doubleEnc(p,key1,key2)
    cryptos.append(c)
    print("plain: " + prettyHex(toInt(p),16) + " \t2des: " + prettyHex(toInt(c),16))

k1, k2 = attack(plains, cryptos)

print("")
if k1 == -1: print("failure")
else: 
    print("found_key1: " + prettyHex(toInt(k1),16))
    print("found_key2: " + prettyHex(toInt(k2),16))

    if(k1 == key1 and k2 == key2): print("success")
    else: print("failure")
