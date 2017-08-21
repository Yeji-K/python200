from os import rename

target_file = input( '이동할 파일명 : ')
newpath = input('이동 경로 : ')

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath + '/' + target_file

try:
    rename(target_file,newname)
    print('이동이 완료되었습니다.')

except FileNotFoundError as e:
    print(e)
