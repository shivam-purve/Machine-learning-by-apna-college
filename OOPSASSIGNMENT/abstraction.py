from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, days_worked, daily_rate):
        self.days_worked = days_worked
        self.daily_rate = daily_rate

    def calculate_salary(self):
        return self.days_worked * self.daily_rate


employees = [
    Intern(40, 150),
    FullTimeEmployee(50000),
    PartTimeEmployee(20, 1000)
]

for emp in employees:
    print(type(emp).__name__, "Salary:", emp.calculate_salary())
