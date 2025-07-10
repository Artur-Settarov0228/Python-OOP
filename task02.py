class Student:
    def __init__(self , name , age , grade ):
        self.name = name
        self.age = age
        self.grade = grade

student = Student("Artur" , 20 , 100)

print(f"{student.name}, {student.age} ,{student.grade}")