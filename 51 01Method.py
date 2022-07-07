from re import A


class DemoClass:
    a=10
    def showvalue(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def showvalu1(self,a,b):
        print(a+b)
        

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)