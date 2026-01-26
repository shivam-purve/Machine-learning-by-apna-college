# sets

# s = {1,2,3,4,5}

# print(type(s))

# print(s)
# print(len(s))

# s1 = {1,2,3,2,3,4,5,2,1}

# print(len(s1))
# print(s1)


#set methods


s = {1,2,2,2,3}

s.add(4)
print(s)
s.remove(2)
print(s)
s.pop()
print(s)

s2 = {5,6,7,8,1,2,3}
s.union(s2)
print(s.union(s2))

print(s.intersection(s2))



s.clear()
print(s)
