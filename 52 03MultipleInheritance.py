#Only support python multilevel

class A:
    def displayA(azmi):  #azmi is argument
        print("Welcome A")

class B():               
    def displayB(azmi):
        print("Welcome B")

class C(A,B):               
    def displayC(azmi):
        print("Welcome C")

obj =C()
obj.displayA()
obj.displayB()
obj.displayC()