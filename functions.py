# #function definition

# def greet():
#     print("Hello, shivam")




# #fun call
# greet()




# def average(a,b,c):
#     avg = (a+b+c)/3
#     return avg


# #fun call
# num1 = float(input("enter first number: "))
# num2 = float(input("enter second number: "))
# num3 = float(input("enter third number: "))


# avg = average(num1,num2,num3)
# print("avearge of three given numbers are:",avg)



#default parameters in function

# def sum(a, b = 1):
#     return a + b


# #fun call
# print(sum(5))
# print(sum(3,5))



#lambda function

# sum = lambda a,b:a + b
# avg = lambda a,b,c:(a + b + c)/3

# print(avg(2,3,4))

# print(sum(3,4))







#sum prblem function

#function to add two num

# def sum(a,b):
#     sum = a+b
#     return sum

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# ans = sum(num1,num2)
# print("sum of given two numbers are: ",ans)



#def to find factorial

def fact(n):
    prod= 1
    i=1
    while(i<=n):
        prod*=i
        i+=1
    return prod



#call 

n = int(input("enter any number: "))

ans = fact(n)
print("factorial of n is: ",ans)