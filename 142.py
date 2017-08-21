f = open('141.txt','r')
h = open( '141_copy.txt','w')

data =f.read()
h.write(data)

f.close()
h.close()
