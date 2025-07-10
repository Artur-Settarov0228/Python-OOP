class Student:
    def __init__(self , name , age ):
        self.name = name
        self.age = age
        


    def show_info(self):
        print(f"{self.name} , {self.age} yoshda") 

s1 = Student("Ali", 15)
s2 = Student("Laylo", 17)
s3 = Student("Javlon", 14)
s4 = Student("Malika", 19)
s5 = Student("Bekzod", 16)

students = [s1, s2, s3, s4, s5]

kattasi = max(students, key=lambda student: student.age)
print("Eng katta yoshdagi talaba:")
kattasi.show_info()

