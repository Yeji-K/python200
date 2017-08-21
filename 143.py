bufsize = 1024
f = open('IMG_1116.JPG','rb')
h = open('IMG_1116_copy.JPG', 'wb')

data = f.read(bufsize)
while data :
    h.write(data)
    data = f. read(bufsize)

f.close()
h.close()
