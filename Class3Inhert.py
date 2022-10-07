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
        Person.__init__(self,name,gender, age)
        self.studentid=studentid
        self.fees=fees

    def StudentInfo(self):
        print("Student ID: {}".format(self.studentid))
        print("Fees: {}".format(self.fees))

# Child class
class teacher(Person):
    def __init__(self, name, gender, age, empid,salary):
        Person.__init__(self,name,gender, age)
        self.empid=empid
        self.salary=salary

    def TeacherInfo(self):
        print("Empid: {}".format(self.empid))
        print("Salary: {}".format(self.salary))

stud_obj=student('Shibin','Male',25,12345,10000)
print("Student Details:")
print("----------------")
stud_obj.PersonInfo()
stud_obj.StudentInfo()

