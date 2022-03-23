#This is Addition or Subtraction of two numbers

print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
choice=int(input("Enter your Choice: "))

if choice==1:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    add = num1 + num2
    print("Addition of {0} and {1} is {2}" .format(num1,num2,add))
elif choice==2:
    num3 = int(input("Enter first number:"))
    num4 = int(input("Enter second number:"))
    sub = num3 - num4
    print("Addition of {0} and {1} is {2}".format(num3, num4, sub))
else:
    print("INVALID ENTERY!")