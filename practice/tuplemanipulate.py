# oDD and Even tuple

lst = []
n = int(input("enter number of elements: "))

i = 0
while(i<n):
    val = int(input("enter value for tuple: "))
    lst.append(val)
    i += 1


tup = tuple(lst)

lst1 = []
lst2 = []




for val in lst:
    if((val %2) == 0):
        lst1.append(val)
    else:
        lst2.append(val)

tup_odd = tuple(lst2)
tup_even = tuple(lst1)

print(f"the odd value tuple is: {tup_odd}")
print(f"the even value tuple is: {tup_even}")