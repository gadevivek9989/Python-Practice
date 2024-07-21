for i in range(10 ,20):
    print('i is now {}'.format(i))

for i in range(10):
    print('i is now {}'.format(i))
    #if you give only one number in the range it takes the start 0 as default

for i in range(10 ,2):
    print('i is now {}'.format(i))
    #in this case we do not get out put

for i in range(0 ,10 ,2):
    print('i is now {}'.format(i))
    #this case a like as slices 2 is the difference as same as slices

for i in range(10 , 0 , -2):
    print('i is now {}'.format(i))
    #in this case as same as slice it goes backwards

#continous to conditions.py

age = int(input('please enter your age'))
if age in range (16,65):
    print('have a good day at home')
else:
    ('enjoy your work')

print('-' * 100)

if age <16 or age > 65 :
    print('have a good day at home')
else:
    print('enjoy your work')