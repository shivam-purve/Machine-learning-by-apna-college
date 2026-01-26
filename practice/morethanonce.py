# more than once appear

def count(list1,val):
    count = 0
    for i in list1:
        if(i == val):
            count += 1
    
    return count



list1  = []
n = int(input("enter number of elemnts: "))
i = 0
while(i<n):
    val = int(input("enter value in list: "))
    list1.append(val)
    i += 1

s = set(list1)
for val in s:
    if(count(list1,val) > 1):
        print(f"{val} is element which appeared {count(list1,val)} many times in list")



