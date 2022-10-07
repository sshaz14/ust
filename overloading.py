class Person: #Parent Class
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age

    def greet(self):
        print("Hello")

       #Child class
class student(Person):
    def __init__(self, name, gender, age, studentid, fees):
        Person.__init__(self,name,gender, age)
        self.studentid=studentid
        self.fees=fees

    def greet(self):
        print("Hello stud")

stud_obj=student('Shibin','Male',25,12345,10000)
stud_obj.greet()


stud_obj1=Person('Sheela','FeMale',35)
stud_obj1.greet()
