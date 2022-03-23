#defining functions
def addition(num1,num2):
    add = num1 + num2
    print("Addition of {0} and {1} is {2}".format(num1,num2,add))

def subtraction(num3,num4):
    sub = num3 - num4
    print("Subtraction of {0} and {1} is {2}".format(num3, num4, sub))

def multiplication(num5,num6):
    mul = num5 * num6
    print("Multiplication of {0} and {1} is {2}".format(num5, num6, mul))

def division(num7,num8):
    div = num7 / num8
    print("Division of {0} and {1} is {2}".format(num7, num8, div))

#creating menu
while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for Division")
    print("Press 5 to Exit")
    choice = int(input("Enter your choice:"))

    if choice==1:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        addition(num1,num2)
    elif choice==2:
        num3 = int(input("Enter the first number:"))
        num4 = int(input("Enter the second number:"))
        subtraction(num3,num4)
    elif choice==3:
        num5 = int(input("Enter the first number:"))
        num6 = int(input("Enter the second number:"))
        multiplication(num5,num6)
    elif choice==4:
        num7 = int(input("Enter the first number:"))
        num8 = int(input("Enter the second number:"))
        division(num7,num8)
    elif choice==5:
        break
    else:
        print("INVALID INPUT!")

