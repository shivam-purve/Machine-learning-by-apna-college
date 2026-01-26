# #conditionals

# age = 21
# if age>= 18:
#     print("you can vote")
#     print("you can drive")
# else:
#     print("you cant vote")


# #use of elif

# color = input("enter color: ")

# if color=="red":
#     print("Stop")
# elif color=="green":
#     print("go")
# elif color=="yellow":
#     print("look")
# else:
#     print("invalid color")


# #finding age-group

# age_person = int(input("enter age of person: "))

# if (age_person < 13):
#     print("person is under age-category of child")
# elif (age_person < 18):
#     print("person is under age-category of teenegers")
# else:
#     print("person is under age-category of adult")


# #username and password check

# username = input("enter username: ")
# password = input("enter password: ")

# if (username == "admin" and password=="pass"):
#     print("Login successful!")
# elif (username != "admin"):
#     print("Wrong Username")
# else:
#     print("wrong assword")


# #multiple of 5 or not

# n = int(input("enter any positive number: "))
# if(n%5==0):
#     print("multiple of 5")
# else:
#     print("not a multiple of 5")



#ternary

# age = 18
# status = "Adult" if age >= 18 else "Not Adult"
# print(status)

#nesting

# username = input("enter username: ")
# password = input("enter password: ")


# if (username == "admin" and password == "pass"):
#     print("LOgin successfull!")
# else:
#     if(username != "admin"):
#         print("wrong username given")
#     else:
#         print("password given is wrong")

    
#largest of three

def get_largest(a, b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


#fun call

a = float(input("enter first number: "))
b = float(input("enter second number: "))
c = float(input("enter third number: "))



print(f"largest of three number is: {get_largest(a,b,c)}")






