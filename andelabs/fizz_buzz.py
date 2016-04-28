def fizz_buzz(n):
  if n % 15 == 0:
    return 'FizzBuzz'
  elif n % 3 == 0:
    return 'Fizz'
  elif n % 5 == 0:
    return 'Buzz'
  else:
    return n

print fizz_buzz(3)
print fizz_buzz(5)
print fizz_buzz(45)
print fizz_buzz(131)
