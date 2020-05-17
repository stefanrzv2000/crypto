k = 1<<15

s = ""

for i in range(k): s = s + "10"

s = s + "\n"

f = open("one-zero.txt","w")
f.write(s)