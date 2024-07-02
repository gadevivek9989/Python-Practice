shopping_list = ['milk','rice','banana','roti','egg','bread']

item_to_find = 'rice'
found_at = None


#for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
         
if found_at is not None :
    print('item found at position {}'.format(found_at))
else:
    print('{} not found'.format(item_to_find))