n=int(input("Enter a number:"))

def fact(n):
    if n<=1:
        return 1
    else:
        fact=n*fact(n-1)
        return n

print("The factorial ",n, "is",fact(n))