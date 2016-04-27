class Person(object):
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
