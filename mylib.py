def add_txt(t1,t2):
    return t1+":"+t2

def reverse(*args):
    print(len(args))
    ret = list(args)
    idx = len(args)-1
    for i in range(len(args)):
        ret[i] = args[idx-i]
    return ret

