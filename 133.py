val = input('문자 코드값을 입력하세요: ')
val = int(val)
try:
    ch = chr(val)
    print('코드값: %d [%s], 문자: %s'%(val,hex(val),ch))
except:
    print('존재하지 않음')
