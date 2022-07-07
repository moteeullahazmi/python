s=input("Enter a Value: ")
reverse= s[::-1]           #slicing methos to used & -1 is backward
print(reverse)
if(s==reverse):
    print("Yes, it is palindrome")
else:
    print("No it is not palindrome")
