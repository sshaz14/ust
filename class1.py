
#Create an employee class

class Employee:
    def __init__(self, name, empid):
        self.name=name
        self.empid=empid

    def greet(self):
        print("Thanks for joining {}".format(self.name))


# Create an Employee object

emp1 = Employee("Arjun", 78923)

print('Name:', emp1.name)
print('Employee ID:', emp1.empid)
emp1.greet()

# Create another Employee Object

emp2 = Employee('Anu', 78924)

print('Name:', emp2.name)
print('Employee ID:', emp2.empid)
emp2.greet()

emp2.country = 'India' # instance variable can be created manually
print(emp2.country)

# Modify Object Properties
emp1.name = 'Aryan'
print(emp1.name)

# Delete Object Properties
del(emp1.empid)
#this will give Attribute Error
#emp1.empid


# Delete an Object
del emp1
#This will give a Name Error
emp1
