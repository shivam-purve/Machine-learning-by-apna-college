#while loops

# count = 1

# while (count <= 5):
#     print("Hello world")
#     count += 1



# print(1 to N)

# n = int(input("enter any number: "))

# i = 1
# while(i <= n):
#     print(i)
#     i+=1


# n = int(input("enter any number: "))

# i = n
# while(i > 0):
#     print(i)
#     i -= 1


#Multiplication table

# n = int(input("enter any number: "))

# i = 1
# while(i <=10):
#     print(n*i)
#     i += 1



# break and continue keyword


# i = 1
# while(i <= 10):
#     if(i %6 == 0):
#         break
#     print(i)
#     i += 1



# i = 1
# while(i <= 10):
#     if(i %3 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
    


#print odd numbers from 1 to n

# n = int(input("enter a number: "))
# i = 1
# while(i <= n):
#     if(i %2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# string = "shivam"

# for var in string:
#     print(var)

# check presence of specific character
# string  = input("enter string: ")

# char = input("enter character you find to check out presence: ")


# if char in string:
#     print("presence in the string")
# else:
#     print("not in string")

# for loop on sequence
# for i in range(10):
#     print(i + 1)


# word = "artificial intelligence"
# count = 0
# for char in word:
#     if(char == 'i'):
#         count+=1

# print("count of i is: ",count)


#vowel count


# string = input("enter a string: ")

# vowels = "aeiou"
# count = 0
# for char in string:
#     if(char in vowels):
#         count += 1

# print("count of vowels is:",count)


# for i in range(10):
#     print(i)

# print("---------")

# for i in range(1,11):
#     print(i)


# print("---------")

# for i in range(1,10,2):
#     print(i)

# print("---------")

# for i in range(2,11,2):
#     print(i)


#sum of first N natural number

n = int(input("enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print("sum of numbers till ",n,"is ",sum)

