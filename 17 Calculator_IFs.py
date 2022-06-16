print('''                        
+ SUM
- SUBSTRACT
* MULTIPLY
/ DIVISON
''')
                                                # IF IF only use a maximum time consumption
num1= int(input("Enter a first number is : "))
num2= int(input("Enter a second number is: "))
opr = input("Choose a Oprator +, -, *, /:  ")
if opr=="+":
    print(num1+num2)
if opr=="-":
  print(num1*num2)
if opr=="+":
    print(num1*num2)
if  opr=="/":
    print(num1/num2)
#else:                            //this line else in / oparator to used else statement
    #print("Invalid Oprator")
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("Invalid Operator")