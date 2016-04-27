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
