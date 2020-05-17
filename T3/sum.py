raw = 40961

s = 0
k = 1

while s < raw:
    s = s + k*2**k
    k = k+1
    print(s)

print("k = " + str(k))
print("compressed = " + str(2**(k+1)))