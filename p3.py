#number comparision using Python
A=input("Enter your first value:")
B=input("\nEnter your second value:")
C=input("\nEnter your third value:")

num1=int(A)
num2=int(B)
num3=int(C)

if(num1>num2 or num1>num3):
    print("\nThe value of A is greatest")
else:
    print("\nThe value of A is smaller among B and C")