import random

highest = 10
answer = random.randint(1 , highest)
print(answer) #this is only to test the code if you not mention you have to guess

print('please guess a number between 1 and 10: ')
guess = int(input()) 

if guess != answer:
    if guess < answer:
        print('please guess higher')
    else: #guess must be greater than the answer
        print('please guess lower')
    guess = int(input())
    if guess == answer:
        print('well done, you have guessed correctly')
    else: 
        print('sorry , you have not guessed correctly')
else:
    print('you got it first time')

#if guess < answer:
#    print('please guess higher')
#    guess = int(input())
#    if guess == answer:
#        print('well done you have guessed it')
#    else:
#        print('sorry, you have not guessed correctly')
#elif guess > answer:
#    print('guess lower value')
#    guess = int (input())
#    if guess == answer:
#        print('well done , you have guessed correctly')
#    else:
#        print('sorry , you have not  guesed correctly')
#else:
#    print('you got it in your first attempt')

     #conditionaal operators
     # comparision operators when testing conditions  < , <= , > , >= , == , !=(not equal to) 






















      



