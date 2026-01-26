import json

# for json_str --> py_obj  &&  py_obj --> json_str



# json_str = '{"name": "shivam", "isTeacher":true}'
# py_obj = json.loads(json_str)
# print(type(json_str))
# print(type(py_obj),py_obj)


# python_obj = {
#     "name":"shivam",
#     "isTeacher":True,
# }

# json_string = json.dumps(python_obj)

# print(type(python_obj))
# print(type(json_string),json_string)

# now we will discuss how to deal with file

# with open("./fileinputoutput/data.json","r") as f:
#     py_obj = json.load(f)
#     print(type(py_obj),py_obj)








##  writing/dumping  (data.py) in to data.json 
import json

data = {
    "name": "shivamraaz",
    "isStudent": None,
    "isTeacher": False,
    "subjects": ["python", "science", "AI/ML"],
    "address": {
        "city": "Madhubani",
        "village": "Basopatti",
        "country": "India"
    },
    "age": 18,
    "isIntelligent": True
}

with open("./fileinputoutput/data.json", "w") as f:
    json.dump(data, f, indent=4,sort_keys = True)



