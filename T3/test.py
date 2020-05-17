import sys

def printbin(x,len):
    s = ""
    b = 1<<(len-1)
    while(b > 0):
        if(x>=b): s = s + "1"; x = x-b
        else: s = s + "0"
        b = b>>1
    return s + " "

argv = sys.argv

print(argv[1])
print(" ")

file = open(argv[1],"r")
s = file.readline()

c0 = 0
c1 = 0

#print(s)

for c in s:
    if(c == '0'): c0 = c0+1
    if(c == '1'): c1 = c1+1

print("zeros, ones")
print(c0,c1)

code = {
    "0" : "0 ",
    "1" : "1 "   
}

d = 1

p = s[0]

comp = str()
compbin = ""
raw = 0
compressed = 0
compressedbin = 0

curlen = 1

ok = 1
for c in s:
    raw = raw + 1
    if(ok or c == '\n'): 
        ok=0
        continue
    if(p+c in code): p = p+c
    else: 
        comp = comp + code[p]
        compressed = compressed+1

        compbin = compbin + printbin(int(code[p]),curlen)
        compressedbin = compressedbin + curlen

        d = d+1
        if(d >= 1<<curlen): curlen += 1
        code[p+c] = str(d) + " "
        p = c
comp = comp + code[p]
compressed = compressed+1

compbin = compbin + printbin(int(code[p]),curlen)
compressedbin = compressedbin + curlen

#print("d = " + str(d))
print("raw = " + str(raw))
#print("compressed = " + str(compressed))
print("compressed = " + str(compressedbin))

print("score = " + str(round(float(compressedbin)/raw,3)))

if compressed < 100:
    for x in code:
        print(code[x] + " : " + x)

    print(comp)
    print(compbin)

print(" ")