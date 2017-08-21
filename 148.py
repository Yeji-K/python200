from os import rename

target_file = '141.txt'
newname = input('새로운 파일이름을 입력하세요.')
rename(target_file,newname)
print('파일명을 변경하였습니다.')
