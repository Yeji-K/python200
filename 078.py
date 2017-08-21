txt = 'abcdefghijk'
ret = txt[::-1]
print(ret)

def reverse(*args):
    ret = []
    print(len(args))
    for i in range(len(args)-1,-1,-1):
        print(i)
        ret.append(args[i])
    return ret


arr = [1,2,3]
print(reverse(1,2,3))

