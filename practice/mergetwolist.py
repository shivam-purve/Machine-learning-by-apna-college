

lst1 = []
lst2 = []

n1 = int(input("enter length of first list: "))
n2 = int(input("enter length of second list: "))

i = 0
while(i<n1):
    val = int(input("enter number in list: "))
    lst1.append(val)
    i += 1

i = 0
while(i<n2):
     val = int(input("enter number in list: "))
     lst2.append(val)
     i += 1


res  = []
for val in lst1:
     res.append(val)

for val in lst2:
     res.append(val)

res.sort()

print(res)
     
