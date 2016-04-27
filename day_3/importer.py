from exporter import super_sum, hello_again, max_min, people

print super_sum, hello_again, max_min, people

a = [10, 3, -2, 50, -20]

print hello_again('Joe', 89)
print hello_again(*people[1])
print super_sum(*a)
print max_min(a)
