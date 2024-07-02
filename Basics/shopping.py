shopping_list = ['milk','rice','banana','egg','roti']

for item in shopping_list:
    print('buy ' + item)

    # to exclude any item we can use this code ther are two ways as line 11 and line 18

shopping_list = ['milk','rice','banana','egg','roti']

for item in shopping_list:
    if item != 'milk':
        print('buy ' + item)


shopping_list = ['milk','rice','banana','egg','roti']

for item in shopping_list:
    if item == 'milk':
        continue
    print('buy ' + item)

print('- ' * 50)

shopping_list = ['milk','rice','banana','rot egg','i']

for item in shopping_list:
    if item == 'egg':
        break

    print('buy ' + item)
     



    
        
