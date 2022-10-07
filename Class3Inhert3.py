class Person: #Parent Class
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        

    def PersonInfo(self):
        print("Name:{}".format(self.name))
        print("Age:{}".format(self.age))
        print("Gender:{}".format(self.gender))

#Child class
class employee(Person):
    def __init__(self, name, age, gender, empid, salary):
        Person.__init__(self,name,gender, age)
        self.empid=empid
        self.salary=salary


    def employeeInfo(self):
        print("Empid: {}".format(self.empid))
        print("Salary: {}".format(self.salary))
        
# Grand Child class
class fulltime(employee):
    def __init__(self, name, age, gender, empid, salary, WorkExperience):
        employee.__init__(self,name,gender, age,empid, salary)
        self.WorkExperience=WorkExperience

    def FullTimeInfo(self):
        print('Work Experience:{}'.format(self.WorkExperience))

# Grand Child class
class contractual(employee):
    def __init__(self, name, age, gender, empid, salary, ContractExpiry):
        employee.__init__(self,name,gender, age,empid, salary)
        self.ContractExpiry=ContractExpiry

    def ContractInfo(self):
        print('Contract Expiry:{}'.format(self.ContractExpiry))


print("Contractual Employee Details:")
print("------------------------------")
contr_obj=contractual('Shibin','Male',25,12345,10000, '31-12-2022')
stud_obj.PersonInfo()
stud_obj.ContractInfo()

