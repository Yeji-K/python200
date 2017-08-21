class MyClass:
    var = '안녕하세요'
    def sayHello(self):
        print(self.var)

    def say(self,str):
        print("MyClass : " + str);


obj = MyClass()
print(obj.var)
obj.sayHello()
obj.say("Hello")
