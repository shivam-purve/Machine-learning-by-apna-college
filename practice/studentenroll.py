

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

s = set()
# for tup in info:
#     s.add(tup[1])


# lists all the unique courses

for name,course in info:
    s.add(course)

print(list(s))

#lists all the students enrolled in english
l = []
for (name,course) in info:
    if(course == "English"):
        l.append(name)

print(l)   

#dict with{student,set of courses}

dic = {}
for name,course in info:
    if(dic.get(name) == None):
        dic.update({name:set()})
        dic[name].add(course)
    else:
        dic[name].add(course)
    
print(dic)







