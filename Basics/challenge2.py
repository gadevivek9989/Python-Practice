print('please select a option from given below')

print('1:/tgo for swiming')
print('2:/tlearn python')
print('3:/teat food')
print('4/thave a bath')
print('0/texit')

while True:
    choice = input ()

    if choice == '0':
        break
    elif choice in '1234':
        print('you chose {}.format(choice)')




