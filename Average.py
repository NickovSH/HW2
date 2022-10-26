#Сalculation of the arithmetic mean
import random

def Average():
    print('\nExercise 1')

    num1 = random.uniform(0,100)
    num2 = random.uniform(0,100)
    num3 = random.uniform(0,100)

    average = (num1+num2+num3)/3

    print('Number 1 = ', num1)
    print('Number 2 = ', num2)
    print('Number 3 = ', num3)
    print('Mean = ', average)