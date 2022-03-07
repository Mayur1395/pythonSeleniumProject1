class calculator:
    def __init__(self, a, b):  # constructor when we declared that time self keyword is automatically their
        self.a1 = a            # when we declared in any variable inside the class we called it self.
        self.b1 = b
        print(self.a1 + self.b1)


    def method1(self):
        print("i am learning python lang")

c1 = calculator(20,10)
c1.method1()

c1.__init__(20,30)