First = input("Enter a number : ")
Operator = input("Enter an operator +,-,*,/,%: ")
Secound = input ("Enter 2nd number : ")
First = int(First)
Secound = int (Secound)

if Operator == ("+"):
    print(First + Secound)

elif Operator ==("-"):
    print(First - Secound)

elif Operator ==("*"):
    print(First * Secound)

elif Operator ==("/"):
    print (First / Secound)

elif Operator ==("%"):
    print (First % Secound)
else:
    print("invalid entry")