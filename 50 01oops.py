 #one class created multiple object

class DemoClass:             #class is keyword used variables
    
    a=10
    def sumvalues(self):     #def keyword is used create a function
        print(20+30) 
demoobject= DemoClass()
demoobject1= DemoClass()      #Calling   small democlass is name anything
print(demoobject.a)
print(demoobject1.a) 
demoobject.sumvalues()  

