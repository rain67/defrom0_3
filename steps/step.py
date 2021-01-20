# step1
import numpy as np

class Variable:
     def __init__(self, data):
         self.data = data
         self.grad = None

data = np.array(1.0)
x = Variable(data)
print(x.data)

# step2

class Function:
    def __call__(self,input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        self.input = input
        return output
    
    def forward(self,x):
        raise NotImplementedError() # forward methodは継承先で作成しないとエラーになる。
    
    def backward(self,gy):
        raise NotImplementedError()


x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))

class Squre(Function):
    def forward(self,x):
        y = x ** 2
        return y

    def backward(self,gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

x = Variable(np.array(10))
f = Squre()
y = f(x)
print(type(y))

# step3 関数の連結

class Exp(Function):
    def forward(self,x):
        y = np.exp(x)
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x)
        return gx

A = Squre()
B = Exp()
C = Squre()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)
print(y.data)

