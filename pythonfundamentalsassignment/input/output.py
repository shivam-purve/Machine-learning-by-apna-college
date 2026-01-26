
# print welcome message

'''name = input("enter your name: ")
age = input("enter your age: ")
welcome_msg = "Hello "+ name + ","+ " you are "+ age +" years old!"
print(welcome_msg) '''

#print sum,difference,product,and quotient
'''
a = int(input("enter a: "))
b = int(input("enter b: "))
sum = a+b
diff = a-b
prod = a*b
quotient = int(a/b)
print("sum is: ",sum)
print("difference is: ",diff)
print("multiplication is: ",prod)
print("quotient is: ",quotient)'''



#find average
'''
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = float(input("enter third number: "))

num1 = float(num1)
num2 = float(num2)

avg = (num1 + num2 + num3)/3
print("average of given three numbers are: ",avg)'''

#type casting-explicit conversion
'''
num_test = input("enter test number: ")
test_integer = int(num_test)
test_decimal = float(num_test)
test_string = str(num_test)

print("values and its type: ",test_integer,type(test_integer))

print("values and its type: ",test_decimal,type(test_decimal))

print("values and its type: ",test_string,type(test_string))
'''

#operator precedence
'''
x = 10 + 3*2**2
print( "value of x is: ", x)
'''



#swap two numbers
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))



# print("before swapping operation numbers are: a = ",a ,"and b = ",b)

# #method-1
# '''
# c = a
# a=b
# b=c
# '''
# #method 2

# a = a+b
# b = a-b
# a = a-b
# print("after swapping operation numbers are: a = ",a ,"and b = ",b)

#temperature conversion
'''
temp_celc = input("enter temperature in celcius: ")
temp_celc = float(temp_celc)

temp_fahr = (temp_celc*(9/5)) + 32
print("value of temperature ",temp_celc,"celcius in fahrenheit is ",temp_fahr)

'''

#Area of circle
'''

PI = 3.14

rad_circ = float(input("enter radius of circle: "))
area_circl = PI*(rad_circ**2)

print("Area of circle with radius ",rad_circ ,"is ",area_circl)

'''
#simple interest calculation
'''
principal = float(input("enter principal amount: "))
rate = float(input("enter rate of interest: "))
time = float(input("enter time duration of interest: "))

simple_interest = (principal*rate*time)/100

print("simple interest calculated as per given amount and rate is: ",simple_interest)
'''

#input/output

num = float(input("enter a decimal number: "))

num_integer = int(num)
num_frac = num - num_integer

print("Integral part of given number is: ",num_integer,"and fractional part is: ",num_frac)

