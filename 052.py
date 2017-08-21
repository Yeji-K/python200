class MyClass:

    def __init__(self, *args):
        self.var = 'TEST'
        self.name = args;
        print( 'MyClass(name) 인스턴트 객체 생성')


obj = MyClass()
print(obj.var)

obj2 = MyClass('철수')
print(obj2.name)

