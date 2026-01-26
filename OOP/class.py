

class Student:


    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        #print("this is constructor\n")

    def get_cgpa(self):
        return self.cgpa
    




stu1 = Student("shivam",9.17)
stu2 = Student("naaguu",8.4)
stu3 = Student("raajuu",7.8)



print(stu1.name,stu1.cgpa)
print(stu2.name,stu2.cgpa)
print(stu3.name,stu2.cgpa)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")