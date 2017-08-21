from os.path import getsize

file1 = '141.txt'
file2 = 'C:/Users/FORCS-NT0223/Desktop/새 폴더/IMG_1116.JPG'

file_size1 = getsize( file1 )
file_size2 = getsize( file2 )

print( 'FileName: %s\tSize: %d' %(file1, file_size1))
print( 'FileName: %s\tSize: %d' %(file2, file_size2))
