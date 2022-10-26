import random

def Division():
    print('\nExercise 2')

    num1 = random.uniform(0, 100)
    num2 = random.uniform(0, 100)

    division = num1//num2
    integer_division = num1%num2

    print('Number 1 = ', num1)
    print('Number 2 = ', num2)
    print('number 1 division number 2 = ', division)
    print('Integer division of number 1 by number 2 = ', integer_division)