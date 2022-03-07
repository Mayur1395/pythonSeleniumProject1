class mayur():
    num = 100

    def method1(self,name):
        print("hello"+" "+ name)

    def method2(self, a, b, c):
        print(a+b+c)

    def method3(self, a, b):
        return (a+b)



m1 = mayur()   # syntax of craeting object of this class and stored in one object
m1.method1("ashwin")   #then called it object name.methodname
m1.num

m1.method2(10,20,30)

x = m1.method3(20,30)
print(x)



