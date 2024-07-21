menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) - 1, -1 , -1):
        if meal[index] == 'spam':
            del meal[index]

    print(', '.join(meal))

#inthis code python automatically print the code by default in form of list by brackets and semi collns 
#to get code in format of nospam_gen add print(', '.jion(meal))

#for meal in menu:
#    for item in meal:
#        if item != 'spam':
#            print(item , end= ', ')

#    print()

#hence sep is not used here because sep(separators) only used in between the values we print