class A:
    def displayA(azmi):  #azmi is argument
        print("Welcome A")

class B(A):               
    def displayB(azmi):
        print("Welcome B")

class C(B):               
    def displayC(azmi):
        print("Welcome C")

obj =C()
obj.displayA()
obj.displayB()
obj.displayC()