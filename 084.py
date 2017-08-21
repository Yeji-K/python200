try:
    while True:
        txt = input('input a sentenct : \n')
        ret1 = txt.upper()
        ret2 = txt.lower()
        print('upper : %s'%ret1, 'lower : %s'%ret2)

except KeyboardInterrupt:
    print('Exit')
