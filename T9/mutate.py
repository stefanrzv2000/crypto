from util import *

ba = readBytes("mac.bmp")

nba = mutate(ba,range(100,200,1))

writeBytes(nba,"mac2.bmp")
