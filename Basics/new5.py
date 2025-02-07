def sayhello(message):
    print("!!" + message)

sayhello("you are baster")



def sum_number(first,second):
    return first + second

value = sum_number(3,5)
print(value)
print(sum_number(2,sum_number(2,7)))

#print(f"hey you are {input('enter your name')}")

#difference b/w print and return//

def greater(a,b):
    if a>b:
        return(a)
    else:
        return(b)
    
def greater1(a,b):
    if a>b:
        print(a)
    else:
        print(b)

    

result = greater(3,4)
print(result)

greater1(5,1)

#another example
def max(a: int,b: int):
    value = a + b
    return value

s=max(6,7)
print(s)



def vivek(message: str,n: int)-> str:
    msg=''
    index=0
    while index<n:
        msg +=message
        index=index+1

    return msg

g=vivek('*',50)
print(g)
