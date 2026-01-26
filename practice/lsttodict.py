

lst = []
n = int(input("enter number of words for list: "))
i = 0
while(i<n):
    fruit = input("enter any word:")
    lst.append(fruit)
    i += 1

dict = {}
for fruit in lst:
    length = len(fruit)
    dict.update({fruit:length})

print(f"all items in dictionary are: {dict.items()}")


   