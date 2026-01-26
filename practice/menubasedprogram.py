#dictionary.py



dict  = {}
n = int(input("enter number of entries in dict: "))

i = 0
while(i<n):
    key = input("enter student name: ")
    value = float(input("enter student mark: "))
    dict.update({key:value})
    i += 1

instr = input("press instructions as A/B/C/D: ")

if(instr == "A"):
    std = input("enter student name for adding: ")
    mark = float(input("enter mark for this student: "))
    dict.update({std:mark})
elif(instr == "B"):
    srch = input("enter student name whose marks to be updated: ")
    mrk = float(input("enter updated marks: "))
    dict[srch] = mrk
elif(instr == "C"):
    srch = input("enter student name whom you want to search for: ")
    print(f"student details are : his/her name is {srch} and his/her marks is {dict[srch]}")
elif(instr == "D"):

    print(f"all list of students and their marks are: {dict.items()}")
else:
    print(f"no valid instruction pressed\n")



