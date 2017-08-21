try:
    while True : 
        msg = input("input a sentence..:")
        msglen = len(msg)
        print('A length of the sentence you inputed is %d.'%msglen)
        print('byte :%d' %len(msg.encode()))
except KeyboardInterrupt:
    print('Bye')
