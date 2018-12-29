num1=input("Enter first num")
num2=input("Enter second num")
op=input("Addition:1\n Subtraction:2\n Multiplication:3\n Division:4")
opertor=int(op)
if opertor == 1:
    print(int(num2)+int(num1))
elif opertor == 2:
    print(int(num2) - int(num1))
elif opertor == 3:
    print(int(num2) * int(num1))
else:
    print(int(num2) / int(num1))