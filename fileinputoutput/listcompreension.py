
#usual list method
squares = []
for i in range(6):
    squares.append(i*i)

print(squares)



#list comprehension method
sq = [ i*i for  i in range(6)]
print(sq)

#odd numbers square

sqo = [i*i for i in range(6) if i%2!= 0]
print(sqo)

#using if ele

nums = [-2,-3,-4,5,7,8,-1]

nums = [0 if val<0 else val for val in nums]
print(nums)

words = ["shivu","apnacollege","raaz","python"]

words = [ word.upper() for word in words]
print(words)