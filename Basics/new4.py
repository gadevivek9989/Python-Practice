name = "there is a lambo in my garage"

the_sssubstring = name[ : -1]

print(the_sssubstring)

if 'lambo' in name:
    print("you are good\n")
    index_of_lambo = name.find("lambo")
    print(f"the index is {index_of_lambo}")
else:
    print("you are toxic\n")


#functions....

def sayhello():
    print('hey hello!')
    print('hello world')

def your_data():
    name=input("enter your name\n")
    age =  int(input("enter your age\n"))
    print("helo " + name + " of ")
    print(age)


sayhello()
your_data()

    