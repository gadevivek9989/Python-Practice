import random

highest = 10
answer = random.randint(1 , highest)
print(answer) #this is only to test the code if you not mention you have to guess

print('please guess a number between 1 and {} '.format(highest))

while guess != answer:
     guess = int(input()) 

     if guess == answer:
          print('you guessed your answer')
          break
     else:
         if guess < answer:
             print('please guess higher')
         else:
              print('please guess lower')    
    




      
      


