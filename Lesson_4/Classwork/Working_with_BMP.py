# -*- coding: utf-8 -*-
import struct
f = open('cat.bmp', 'rb')
d = f.read()
print d[:14]
print struct.unpack("<ccihhi", d[:14])
print len(d)
struct.unpack("<iiihhiiiiii", d[14:54])
print 560 * 362
print 608160 / 3
d2 = d[:54] + (len(d) - 54)*'\xff'
open("gg.bmp", "wb").write(d2)
d2 = d[:54] + (len(d) - 54)*'\x00'
open("gg.bmp", "wb").write(d2)