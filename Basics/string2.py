parrot = 'black mamba'
#         012345678910
                    
print()

print(parrot[4])
print(parrot[10])
print(parrot[2])
print(parrot[9])

print()

print(parrot[-7])
print(parrot[-1])
print(parrot[-9])
print(parrot[-2]) 

print()

print(parrot[4 - 11])
print(parrot[10- 11])
print(parrot[2 - 11])
print(parrot[9 - 11])

#in this three ways you are going to get same answer

#slices in string
#this concept includes start,stop and step 
print()

print(parrot[3 : 8])   #3 is a start point letter and 8 is end point letter with out including the letter 8
print(parrot[0 : 8])
print(parrot[: 8])     #from line 32 and 33 there is no difference if you not give the value of start it takes default from start and #semi colon is stop sign
print(parrot[6 : 8])

print(parrot[6 : 11])
print(parrot[6 : ])   #from the line 36 and 37 we get same answer because in line 37 if we not mention the ending lrtter number it will default to last letter we get in bot lines answer #mamba

print(parrot[ : ])
print(parrot[ : 6] + parrot[6 : ])

#slicing with negative numbers

print(parrot[-5 : -1])
print(parrot[-5 : ])
print(parrot[-8 : -2])
print(parrot[-9 : -2])
print(parrot[2 : -2])
print(parrot[ : -4])

#slicing using steps

print(parrot[0 : 8 : 2])



#          start : stop : step

print(parrot[2 : 7 : 2])

numbers = '9,567;678:564 214,345:651'

print(numbers[ 1 :: 4])
seperators = numbers[1 :: 4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in numbers).split()
print([int(val) for val in values])