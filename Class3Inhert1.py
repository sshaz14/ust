class Person: #Parent Class
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age

    def PersonInfo(self):
        print("Name:{}".format(self.name))
        print("Age:{}".format(self.age))
        print("Gender:{}".format(self.gender))

#Child class
class student(Person):
    def __init__(self, name, gender, age, studentid, fees):
        super().__init__(name,gender, age)
        self.studentid=studentid
        self.fees=fees

    def StudentInfo(self):
        super().PersonInfo()
        print("Student ID: {}".format(self.studentid))
        print("Fees: {}".format(self.fees))


stud_obj=student('Shibin','Male',25,12345,10000)
print("Student Details:")
print("----------------")

stud_obj.StudentInfo()

