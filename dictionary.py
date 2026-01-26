#disctionary


info = {"name" : "shivam" , "cgpa" :9.2 , "subjects" :["maths", "english", "science"] , "rollNumber" : "CS24B055" , 3.14 : "PI"}

print(type(info))

print(info)

print(info["subjects"])

info["cgpa"] = 9.17
print(info)


print(info.keys())

dict_keys = list(info.keys())

print(type(dict_keys))

dict_vals = list(info.values())

print(type(dict_vals))

print(dict_vals)

#key,val pairs

print(info.items())

# get method from key -> val access

print(info.get("cgpa"))

#print(info["cgpa2"])

print(info.get("cgpa2")) # still run frther code even after error

info.update({
    "city":"Madhubani"
})

print(info)