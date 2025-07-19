num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
num1=float(num1)
num2=float(num2)
print("Addition: ",int(num1+num2))
print("Subtraction: ",int(num1-num2))
print("Multiplication: ",int(num1*num2))
if(num2==0):
    print("Division not possible")
else:
    print("Division: ", int(num1 / num2))