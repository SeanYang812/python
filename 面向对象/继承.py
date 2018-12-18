

class Person:
    def skill(self):
        print("teacher name is %s"%self.name)

    def f1(self):
        self.skill()


class Teacher(Person):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

teacher = Teacher('sean',18,'male')
print(teacher.name)
teacher.skill()
print(teacher.skill())
print(teacher.__dict__)

print(teacher.f1())

class Student(Person):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

student = Student('yang',18,'male')

print(student.name)