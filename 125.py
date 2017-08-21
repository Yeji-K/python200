names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly':7855}

del names['Mary']

try :
    print(names['Mary'])
except :
    print( 'Exception' )
