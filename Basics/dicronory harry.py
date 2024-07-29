d = {}  #empty dictionary
marks = {'vivek' : 99,
         'vikas' : 34,
         'anitha' : 29,
         'sunil' : 12,
         0 : 'barathamma'}

print(marks , type(marks))

print(marks.items())   #it will print in the form of strings and dictionaries  are mutable
print(marks.keys())    #keys are the names or integers before semi colon
print(marks.values())   #values are the integers or names after semi colon

marks.update({'anitha' : 100 , 'sunildaddy' :101 }) #by using this we can add other marks in dictionary or change the marks or name in dictonary
print(marks)

print(marks['vikas'])

#print(marks.get('malya'))  #it gives none if you enter the name that not in dictonary 
#print(marks['malya'])      #it gives error if you enter the name that not in dictonary line 18 and 19 are different gives different output important for interwiews


print(marks.pop('vikas'))  #by this method it prints the value the marks of vikas
print(marks.pop('vikas' , 'malya'))  #in this it gives the marks of vikas and if not in dictionary prints default as the string

print(marks.popitem())  #Removes and returns a (key, value) pair from the dictionary. Pairs are returned in LIFO (Last In, First Out) order in otherwords it prints last key and value in the dictionary
