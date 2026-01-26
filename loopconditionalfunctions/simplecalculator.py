# calculator program

def calculator(a,b,operation):
    # a = int(a)
    # b = int(b)
    if(operation == "+"):
        return a+b
    elif(operation == "-"):
        return a-b
    elif(operation == "*"):
        return a*b
    elif(operation == "/"):
        return a/b
    else:
        print("undefined operation")



#fun call


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

ans = calculator(num1,num2,operator)

print("anser of following operation: ",round(ans,3))