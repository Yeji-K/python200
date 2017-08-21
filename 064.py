h1 = hex(97)
h2 = hex(98)

ret1 = h1 + h2
print(ret1)

a = int(h1,16)
b = int(h2,16)
ret2 = a + b

print( type(ret2) )
print( type(hex(ret2)) )
print('10 : %d / hex : %s' %(ret2, hex(ret2)))
