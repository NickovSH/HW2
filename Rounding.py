#A program that rounds numbers

import random

def Rounding():
    print('\nExercise 3 - Rounding')

    num1 = random.uniform(0, 100)
    print('Random number = ', num1)
    aroundNum1 = round(num1, 2)
    print('Rounding to the second decimal place = ', aroundNum1)
    print('Rounding to the nearest integer = ',round(num1))
    print('Zero padding = ', '{0:=011}'.format(aroundNum1))