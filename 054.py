class Add:
    def add(self, n1, n2):
        return n1+n2

class Multiply(Add):
    def multiply(self,n1,n2):
        return n1*n2


class Calculator(Multiply):
    def sub(self,n1,n2):
        return n1-n2
    

obj = Calculator()
print(obj.add(1,2))
print(obj.sub(1,2))
print(obj.multiply(1,2))
