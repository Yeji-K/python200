names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly':7855}

vals = names.values()
print(vals)
print(type(vals))
vals_list = list(vals)
ret = sum(vals_list)
print('출생아 수 총계: %d'%ret)

print( 'pattern_test:{}'.format(vals_list))
