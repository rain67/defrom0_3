# step1
import numpy as np

class Variable:
     def __init__(self, data):
         self.data = data

data = np.array(1.0)
x = Variable(data)
print(x.data)

# step2

class Function:
    def __call__(self,input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output
    
    def forward(self,x):
        raise NotImplementedError() # forward methodは継承先で作成しないとエラーになる。


x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))

class Squre(Function):
     def forward(self,x):
         return x ** 2

x = Variable(np.array(10))
f = Squre()
y = f(x)
print(type(y))

# step3 関数の連結
