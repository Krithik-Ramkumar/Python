
import math

import Calc 

ArthFunction = Calc.Calc()
   
oper_list = ["+", "-", "*", "x", "/", "**", "^"]


print("-" * 50)
x = float(input("Enter First Number: "))
operator = str(input("Enter Operator: "))
y = float(input("Enter Second Number: "))
print("-" * 50)

if  operator in oper_list or operator in trig_list:
    
    if operator == oper_list[0]:
        ArthFunction.add(x, y)

    elif operator == oper_list[1]:
        ArthFunction.subtract(x, y)
    
    elif operator == oper_list[2] or operator == oper_list[3]:
        ArthFunction.multiply(x, y)

    elif operator == oper_list[4]:
        ArthFunction.divide(x, y)

    elif operator == oper_list[5] or operator == oper_list[6]:
        ArthFunction.exponent(x, y)



else:
    print("Invalid Syntax. Enter a valid operator from our list or Enter a valid number.")
    print(oper_list)
    print("-" * 50)
    exit("Thanks for using my calculator")


    
print("-" * 50)
print("Thank you for using my Calculator")
print("-" * 50)
