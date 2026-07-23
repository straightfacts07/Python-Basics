#instead of letting user crash the program we should add exception to handle
#those edge cases

try:
    age=int(input('age: '))
    income=20000
    risk=income/age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('age cannot be zero')

