
# #intro to list
# marks = [99,89,100,65,92]
# print(type(marks))
# print(marks)
# print(len(marks))

# #slicing in lists
# infos = ["shivam" , 18 , 9.17 , "Nagu"]
# print(infos[:3])
# print(infos[:])

# print(infos[-4:])
# print(type(infos))

#list methods

# num = [1,2,0]
# num.append(5)
# print(num)

# num.insert(2,3)  #l.insert(idx,val)
# print(num)

# # num.sort() #sort in increasing order

# num.sort(reverse = True)
# print(num)

# num.reverse()
# print(num)

# nums = [1,2,3,10,4]

# for val in nums:
#     print(val)


# search pblm

x = 10

nums = [1,2,3,10,4]
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} is at index {idx}")
        break
    
    idx += 1

