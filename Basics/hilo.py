low = 1
high = 1000

print('please think a number between {} and {}'.format(low,high))
input('press enter to start')

guesses =1
while low != high:
    print('\tguessing in the range of {} to {}'.format(low , high))
    guess = low + (high - low)//2
    high_low = input('my guess is {}.should i guess higher or lower enter h or l, or c if my guess was correct'.format(guess)).casefold()

    if high_low == 'h':
        low = guess + 1

    elif high_low == 'l':
        high = guess - 1


    elif high_low == 'c':
        print('i got it in {} guesses'.format(guesses))
        break

    else:
        print('please enter h,l or c')
    guesses = guesses +1

else:
    print('you thought of the number {}'.format(high))
    print('i got it in {} guesses'.format(guesses ))

      

