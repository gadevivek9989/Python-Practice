#strings aare immutable when we tried to change a string python created a new object a new string and reattached the name to it

#listes are mutaable they can be changed when we appended a new item python was able to change the contents of the lists with out creating a new one

shopping_list = ['bread','milk','banana','chocolaate','biscuits'] 
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ['butter']
print(shopping_list)
print(id(shopping_list))
print(another_list)


a = b = c = d = e =f = another_list

print(a)
print('adding cream')
b.append('cream')
print(c)
print(e)
