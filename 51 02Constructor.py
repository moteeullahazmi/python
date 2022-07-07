class DemoClass:
    a=10
    def __init__(self):                #__init__ this function is used constructor which are automatic called.
       print("Wecome to Azmian")    
    def showvalue(self):
        print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def showvalu1(self,a,b):
        print(a+b)
        

obj=DemoClass()
obj.showvalue()
obj.showvalue1(20,30)