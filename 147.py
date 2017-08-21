from os import remove

target_file = '141_copy.txt'
k = input('[%s] 파일을 삭제하시겠습니까?' %target_file)

if( k == 'y'):
    remove(target_file)
    print('[%s] 파일을 삭제하였습니다' %target_file )
