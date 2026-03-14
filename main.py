class Student:
    amount_of_students = 0
    print("Hi")
    def __init__(self, h = 120):
        Student.amount_of_students = Student.amount_of_students + 1
        self.height = h
    def grow(self, height = 120):
        self.height = height + 10
Nick = Student(h=180)
Kate = Student(h=190)
Max = Student()
print(Nick.height)
print(Kate.height)
print(f"Max h={Max.height}")
Max.grow()
print(f"Max h={Max.height}")
print(Student.amount_of_students)

