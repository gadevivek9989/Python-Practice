marks1 = int(input('please enter you marks'))
marks2 = int(input('please enter you marks'))
marks3 = int(input('please enter you marks'))

total_percentage = (100*(marks1 + marks2 + marks3)/300)

if (total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print('you have passed',total_percentage)

else:
    print('you failed tyr in supply',total_percentage)