try:
    while True:
        numstr = input('input Number : ')
        print(  type(numstr) )
        try:
            num = int(numstr)
            print('A number is Double <%d>' %num)
        except:
            try:
                num = float(numstr)
                print('A number is Float <%f>' %num)
            except:
                print('Your Input is not a number')
except KeyboardInterrupt:
 
