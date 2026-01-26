# tuple

tup = (1,2,3,4,5)

print(tup)
print(type(tup))  # <class,tuple>
print(len(tup))
print(tup[2])


#immutable

# tup[1] = 5 #XxXXX

# single valued tuple

tup = (1)    #will treat it as int not tuple
print(type(tup))   #<class,int>


tup = ("abc",) # now treat it as tuple
print(type(tup))


# slicing
tup = (2,4,5,7,10,50)

print(tup[:3])

print(tup[:])  #default total tuple print


for val in tup:
    print(val)



#sum of all elemennts of tuple

sum = 0
for val in tup:
    sum += val
print(f"sum of {len(tup)} elements of tuple is {sum}")


# tuple methods

tup1 = (1,2,3,4,5,2,3,4,2)

print(tup1.index(3))


print(tup1.count(2))