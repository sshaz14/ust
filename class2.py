import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, phone, email):
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.address=address
        self.phone=phone
        self.email=email

    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        if today<datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age-=1
        return age

person = Person('Arif', 'Ahmed', datetime.date(1994, 2, 18),'jhjshdjsd jsn djsnds nsndks', '1234567890', 'arif.ahmed@example.com')
print(person.name)
print(person.email)
print(person.age())
                
