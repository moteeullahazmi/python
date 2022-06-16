print('''
+ SUM
- SUBSTRACT
* MULTIPLY
/ DIVISON
''')

num1= int(input("Enter a first number is : "))
num2= int(input("Enter a second number is: "))
opr = input("Choose a Oprator +, -, *, /:  ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
  print(num1*num2)
elif opr=="+":
    print(num1*num2)
elif  opr=="/":
    print(num1/num2)
else:
    print("Invalid Oprator")
