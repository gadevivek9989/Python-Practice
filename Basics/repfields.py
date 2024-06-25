#imp point
#numbers cant be concatenated with strings using +
#one approach we could take is to coerce our numbers into a string using str function

age = 24 
print('my age is ' + str(age) + ' years')

print('my age is {0} years '.format(age))

print('there are {0} days in {1} , {2} , {3} , {4} , {5} , {6} and {7}'
      .format(31 , 'jan' , 'feb' , 'mar' , 'apr' , 'may' , 'oct' , 'dec' ))

#in our code we replaced 8 gaps numbered 0 to 7
#these are replaced by the words after .farmat
#the first value goes to {0} abd second to{1} and so on

print('jan: {1}, feb: {2}, mar: {0}, apr: {1}, may: {2}, jun: {0}'
     .format(29,30,31))

print("""jan: {1}
 feb: {2}
 mar: {0}
 apr: {1}
 may: {2}
 jun: {0}""".format(29,30,31))
