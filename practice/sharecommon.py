
list1 = []
list2 = []

n1 = int(input("enter number of list1 element: "))
n2 = int(input("enter number of list2 element: "))

i = 0
while(i<n1):
    val = int(input("enter a number: "))
    list1.append(val)
    i += 1

i = 0
while(i<n2):
    val = int(input("enter a value to append in list: "))
    list2.append(val)
    i += 1


set1 = set()

for val in list1:
    set1.add(val)


for val in list2:
    set1.add(val)


length = len(set1)

if( (n1 + n2) > length ):
    print(f"lists share common elements\n")
else:
     print(f"lists share  no common elements\n")


