#The program reverses the number

maxInt = 2147483647
minInt = -2147483647

def Reverse():
    print('\nExercise 4 - Reverse the number')

    try:
        print('Enter a positive or negative number with a minus = ')
        num = int(input())

        if num > maxInt or num < minInt:
            numReversed = 0
            print('Inverted number = ', numReversed)

        elif num >= 0:
            num = str(num)
            numReversed = ''.join(reversed(num))
            print('Inverted number = ', numReversed)

        elif num < 0:
            num = str(num)
            num = num[1:]
            numReversed = ''.join(reversed(num))
            print('Inverted number = ', '-' + numReversed)




    except Exception:
        print('You didn\'t enter a number')
