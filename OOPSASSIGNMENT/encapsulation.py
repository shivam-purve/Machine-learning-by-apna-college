class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # ---------- Getter methods ----------
    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks

    # ---------- Setter methods with validation ----------
    def set_name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name

    def set_roll_no(self, roll_no):
        if not (1 <= roll_no <= 100):
            raise ValueError("Roll number must be between 1 and 100.")
        self._roll_no = roll_no

    def set_marks(self, marks):
        if marks < 0:
            raise ValueError("Marks cannot be negative.")
        self._marks = marks


try:
    student1 = Student("Shivam", 25, 88)

    print("Name:", student1.get_name())
    print("Roll No:", student1.get_roll_no())
    print("Marks:", student1.get_marks())

    # Invalid cases
    # student1.set_marks(-10)
    # student1.set_roll_no(120)
    # student1.set_name("")
except ValueError as e:
    print("Error:", e)
