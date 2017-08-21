import time
class MyClass:
    def __init__(self):
        print( 'init' )

    def __del__(self):
        print( 'del' )


obj = MyClass()

time.sleep(3)
print('del Class...')

del obj
