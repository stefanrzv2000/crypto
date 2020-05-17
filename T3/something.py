from random import randrange

k = 2**16

s = ""

'''
for i in range(k):
    a = randrange(0,2)
    s = s + str(a)
'''

def to_bin(nr,len):
    rez = ""
    for i in range(len):
        rez = rez + str(nr%2)
        nr = nr/2
    return rez

for k in range(12):
    for i in range(2**k):
        t = to_bin(i,k)
        s = s + t + t
        #print(to_bin(i,k))

f = open("twos.txt","w")
f.write(s)