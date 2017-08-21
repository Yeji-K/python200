b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode()

print(type(b_txt))

print(u_txt)

txt = input('1 : ')
b_input = txt.encode()
for cd in b_input:
    print(cd,end=' ')


b_input = input( "incode : " )
print( bytes(b_input).decode() )

