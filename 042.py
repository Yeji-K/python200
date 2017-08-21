def reverse(*args):
    ret = list(args)
    length = len(args) - 1
    for i in range(len(args)):
        #print(length-i)
        ret[i] = args[length-i]
    return ret
ret = reverse('a','b','c','d')
print(ret)

r1,r2 = reverse('A','B')
print('결과값은 %s,%s 입니다.'%(r1,r2))
