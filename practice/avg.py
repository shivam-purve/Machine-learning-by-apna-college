# average of list


n = int(input("enter number of elements in a list: "))
lst = []

i = 0
while(i<n):
    val = int(input("enter number for list: "))
    lst.append(val)
    i += 1

sum = 0
for val in lst:
    sum += val

avg = sum/n
print(f"average of all numbers in list is {avg}")