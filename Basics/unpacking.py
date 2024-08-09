a = b= c= d= e= f= 42
print(b)

x , y , z = 1 , 2 , 69
print(x)
print(y)
print(z)

print('unpacking a tuple')

data = 1 , 2 , 69  #data represents a tuple
x , y , z = data
print(x)
print(y)
print(z)  

print('unpacking a tuple')

data_list = [1 , 2, 69]    #you cant unpack alist because it is mutable you cant know no.of items in the list but in tuple you can sucessfully unpack
#data_list.append(35)

x , y , z  = data_list
print(x)
print(y)
print(z)