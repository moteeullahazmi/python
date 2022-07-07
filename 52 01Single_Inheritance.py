class A:
    def displayA(azmi):  #azmi is argument
        print("Welcome A")

class B(A):               #A is parent of and add the beahaviour
    def displayB(azmi):
        print("Welcome B")



obj =B()
obj.displayA()
obj.displayB()
