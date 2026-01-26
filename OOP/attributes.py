class Student:
    college_name = "ABC College"  #class Atribute
    PI = 3.1

    def __init__(self,name,cgpa):
        self.name = name
        self.gpa = cgpa

        self.PI = 3.14
    


stu1 = Student("shivu",9.17)


print(stu1.name)

print(f"college name called using class attribue ",Student.college_name)

print(f"college name called using instance attribute", stu1.college_name)

print(stu1.PI)  #priority will be given to instance value of PI
print(Student.PI)  #forcefully called by class Name so value in Class attribute will be priorotised
