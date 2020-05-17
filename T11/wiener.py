from util import gen_rsa_wien

n,p,q,e,d = gen_rsa_wien()

print("\n\nstarting attack\n")

print("d = " + str(d) + "\n")

def continued(x,y):

    a = [0,1]
    b = [0,0,1]

    r = 1
    i = 2
    while r > 0:
        r = x%y
        qi = x//y
        x = y
        y = r
        ai = qi*a[i-1] + a[i-2]
        bi = qi*b[i-1] + b[i-2]

        a.append(ai)
        if(i > 2): b.append(bi)
        i = i+1

    return a,b

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def cond(xl,xd,xe,xn):

  # print("xl = " + str(xl))
  # print("xd = " + str(xd))
  # print("xe = " + str(xe))
  # print("xn = " + str(xn))

  xaa = xl
  xbb = xe*xd-1-xl*(xn+1)
  xcc = xl*xn

  delta = xbb*xbb - 4*xaa*xcc
  # print("aa = " + str(xaa))
  # print("bb = " + str(xbb))
  # print("cc = " + str(xcc))
  # print("delta = " + str(delta))
  return is_square(delta)

aa,bb = continued(e,n)
# print(aa[:10])
# print(bb[:10])

# #aa,bb = continued(e,n)
# print(len(aa))

ll=0
dd=0

for i in range(len(aa)-3):
  xl = aa[i+3]
  xd = bb[i+3]
  if(cond(xl,xd,e,n)): ll=xl;dd=xd;break

if(ll==0): print("attack failed")
else: print("success: d = " + str(dd))
