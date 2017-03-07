class Person(object):
    addharno = ""
    def __init__(self, empid, name, pan):
        self.empid = empid
        self.name = name
        self.pan = name
    def setAdg(self,aadhar=""):
        Person.addharno = aadhar



class adharPerson(Person):
    def __init__(self,empid, name, pan,aadhar):
        Person.__init__(self,empid, name, pan)
        self.aadhar = aadhar


newpers = Person(empid=1234,name="Sesh",pan="AE7PP8658")
newpers1 = adharPerson(empid=12344,name="ssss",pan="XVWF124A",aadhar='22437788')

print(newpers)

def EmployeePerson(name , **kwargs ):
    print(name)
    print(kwargs)
EmployeePerson(name="tt", id=123, pan=123)
EmployeePerson(name="tt", empid=12344, pan="XVWF124A", aadhar='22437788')

class reverseString(object):
    def __init__(self,strdata):
        self.strdata = strdata
        self.index = len(strdata)
    def __iter__(self):
        return self
    def  __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.strdata[self.index]

rev = reverseString("Spammer")
revitr = iter(rev)
try:
    while True:
        print(next(revitr))
except(StopIteration):
    pass

class Animal(object):
    def __init__(self,breed):
        self.breed = breed
    def what(self):
        print("I am animal")
    def eat(self):
        print("I am eating")
    def __str__(self):
        print("My breed is {0}".format(self.breed))
class Dog(Animal):
    def __init__(self,breed, name):
        Animal.__init__(self, breed="Husky")
        self.name = name
        print("my name is {0}".format(self.name))
    def what(self):
        print("What is {0} dog doing".format(self.name))
    def bark(self):
        print("I am barking dog")

d = Dog(breed='Hussy', name="Sammy")
#print(d)
d.bark()
d.eat()
d.what()
# print(next(revitr))
# print(next(revitr))
# print(next(revitr))
# print(next(revitr))


# for chars in rev:
#     print(chars)
