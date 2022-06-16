from typing import List


a= 5
                       # datay type is checked by.   type() function.
print(a, type(a))

c=5.5
print(c, type(c))

b=2+5j
print(b, type(b))

                        #string: String is a collection in single qoute, double qoute, three qoute.
                        #multiple line: using three qoute.

s= "Hello@123"
print(s, type(s))

a= '''Welcome To Azmi Wala
          to triple line 
              India Azmi Wala '''
print(a)                
                         #LIST: list is mutable data type and order sequence data and use always define [] (Square bracket)
l=[10,'ws', 5.5]
l[2]=20
print(l,type(l))

                        #TUPLE: tuple is immutable datatype
t=(21,a,3.5)
print(tuple, type(t))

t=(10)                   # this is not tuple because, this is only one store valued

                          #DICTIONARY: dictionary is unordered collection of key-value pair
                          #In python defined as {} each item being a pair in the form KEY:VALUE

d = {
    'azmi': 4,
    'month': 10
}
print(d,type(d))

                         #SET: unorder collection
                                #immutable
                                #unique element
                                #remove duplicate value
                                # {} use bracket
s={10,30,50,10}
print(s,type(s))
