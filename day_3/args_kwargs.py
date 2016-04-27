def hello(name, age, class_=''):
    '''
    .....
    '''
    if class_ != '':
        return "I am {}, and I'm {}, and in class {}".format(name, age, class_)

    return "I am {}, and I'm {}".format(name, age)


people = [("Jane", 23, 'high'), ("Joe", 25), ("Brian", 60), ("Betty", 25, 'low')]

# for x, y in people:
#     print hello(x, y)

# unpacking
for person in people:
    print hello(*person)


def super_sum(*args):
    '''
    Takes in a variable number of items,
    and returns the sum.
    e.g super_sum(10, 20) = 30
        super_sum(10, 20, 40) = 70
        super_sum(1, 4, 5, 6, 7) = 23
    '''
    total = 0
    for i in args:
        total += i

    return total

print super_sum(10, 20)
print super_sum(10, 20, 40)
a = [10, 40, 60]
print super_sum(*a)
b = (10, 30, 60, 100)
print super_sum(*b)


def hello_again(**kwargs):
    return "I am {}, and I'm {}".format(kwargs['name'], kwargs['age'])

joe = {'name':'Joe', 'age':45}
print hello_again(**joe)
print hello_again(name='Joe', age=20)
print hello_again(age=23, name='Syl')

other_people = [
        {'name':'Joe', 'age':45},
        {'name':'Jo', 'age':5},
        {'name':'Joey', 'age':12}
    ]

for i in other_people:
    print hello_again(**i)
