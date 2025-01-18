from math import sqrt

while True:
    num=int(input('Enter a number\n'))

    if num>=9:
        sqrt(num)
        print(f'the square root of number is: {sqrt(num)}')

    else:
        print(f'{num}')
        break