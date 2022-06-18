#isAlpha() : is check a string all is alpha
a="Welcomme to azmi"
w=a.isalpha()
print(w)

#isdigit() : is check all value is digit
b="1234567890"
w=b.isdigit()
print(w)

#isalnum() : is check all value is num & digit
c="123AZMIIndian"
w=c.isalnum()
print(w)

d="oye@ 786"     #false because check @ and space
print(d.isalnum())