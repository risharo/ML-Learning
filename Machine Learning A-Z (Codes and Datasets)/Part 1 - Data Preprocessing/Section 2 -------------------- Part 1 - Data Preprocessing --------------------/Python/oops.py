
class Student:
    name = 'Aman'
    age = 15
    batch = "PCM"

s1 = Student()
print(s1.age)

class Student2:
    def __init__(self,naam):
        self.name = naam
        print("Ok this is the new student name")

s2 = Student2(input())
print(s2.name)
