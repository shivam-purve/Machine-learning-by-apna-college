## multiple inheritence

class Teacher:
    def __init__(self,salary):
        self.salary = salary



class Student:
    def __init__(self,cgpa):
        self.cgpa = cgpa

class TA(Teacher,Student):
    def __init__(self,salary,cgpa,name):
        super().__init__(salary)  #called with super() keyword then no need to pass self

        Student.__init__(self,cgpa)  # self also passed as parameter as constructor called with class Name
        self.name = name
    

ta1 = TA(15_000,9.3,"shivam")
print(ta1.name,ta1.salary,ta1.cgpa)















### multilevel inheritence

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"



# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role = role


# class Accountant(AdminStaff):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary = salary


    

# acc1 = Accountant(25_000,"CA")

# print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)
