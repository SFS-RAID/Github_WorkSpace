class cl1:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        pass
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
        
print('hello')
o1 = cl1()
o1.f1()
o2 = cl1(17, 28)
print(o2.x)