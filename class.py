class student:
    stream = "CSE"
    def __init__(self,roll):
        M=20
        self.age=M+5
        self.roll=roll
        self.stream="IT"
    def disp(self):
        print("\nAge:",self.age)
        print("Roll no:",self.roll)
        print("Branch:",self.stream)
a1 = student(101)
b1 = student(102)
print(a1.stream)
print(b1.stream)
print(student.stream)
print(a1.roll)
print(b1.roll)
a1.disp()