# #strings

# word1 = "python"

# print(len(word1))
# print(word1 + " " + "Hello")

# # for ch in word:
# #     print(ch)

# word = "I study from Apnacollege"
# print(word[13:25])

# print(word[:])
# print(word[13:])


# print(word[-4:-2])


#formatting

print("language is {}".format("python"))

a = 5
b = 10

sum = a + b


print("sum is {}".format(sum))
print("sum of {} and {} is {}".format(a,b,sum))

#index based formatting

print("sum of {1} and {0} is {2}".format(a,b,sum))
#value based formatting

print("values of vars {a} and {b}".format(a = 5, b = 10))

#F-string // literal string interpolation

num1= 5
num2 = 10

print(f"average of numbers {num1} and {num2} are {(num1 + num2)/2}")


