class Employee:
    def get_designation(self):
        print("designation  = Employee")


class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

    
t1 = Teacher()
t1.get_designation()   # called by object so obviously object implementation will executed

# Teacher.get_designation()