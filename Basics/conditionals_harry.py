a = int(input('please enter your age'))
#if statement no.1
if(a%2 == 0):
    print('the number is even')

#end of if statement no.1

#if statement no.2
if (a>=18):
    print('you are able to participate in the consent')

elif (a<0):
    print('age entered is invalid')

elif (a==0):
    print('you are entering your age as 0')

else:
    print('you are not able to participate in the consent')
#end of if statement no.2

print('end of the game')

