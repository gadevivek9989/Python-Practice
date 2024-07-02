numbers = [1 , 24, 35,46,98,90]
for number in numbers:
    if number %8 == 0:
        print('the numbers are not accepted')
        break
else:
    print('these are accepted')