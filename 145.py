spos = 10
size = 10
f = open('141.txt','r')
h = open('145.txt','w')

f.seek(spos)
data = f.read(size)

h.write(data)

h.close()
f.close()
