a1 = int(input('please enter a number'))
a2 = int(input('please enter a number'))
a3 = int(input('please enter a number'))
a4 = int(input('please enter a number'))

if (a1>a2) and (a1>a3) and (a1>a4):
    print('greatest number is a1' , a1)

elif (a2>a1) and (a2>a3) and (a2>a4):
    print('greatest number is a2' ,a2)

elif (a3>a1) and (a3>a2) and (a3>a4):
    print('greatest number is a3' ,a3)

elif (a4>a1) and (a4>a2) and (a4>a3):
    print('greatest number is a4' ,a4)

else:
    print('all are equal')




