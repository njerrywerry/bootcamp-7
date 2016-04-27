class Person:
    """docstring for Person"""
    # class variable
    people_count = 0

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Person.people_count += 1

    # formatting object output
    def __repr__(self):
        return "<object: {}, {}>".format(self.name, self.age)

    def say_hello(self):
        return "Hello, I'm {} and I'm {} years old".format(self.name, self.age)

p1 = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 45)

print p1.say_hello()

a = [('Joe', 23), ('Jane', 23), ('George', 45), ('Njeri', 22), ("Jee", 21), ('Josh', 34)]

b = []
for name, age in a:
    person = Person(name, age)
    b.append(person)

print Person.people_count
print b

for peeps in b:
    print peeps.say_hello()
