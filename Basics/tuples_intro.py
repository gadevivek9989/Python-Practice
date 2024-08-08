name = 'tim'
age = 10

print(name , age , 'python' , 2020)
print((name, age , 'python', 2020))

welcome = 'welcome to my nightmare' , 'alice cooper' , 1975
bad = 'bad company', 'bad company',1947
budgie = 'nightflight', 'budgie' , 1981
imelda = 'more mayhem', 'emilda may',2011
metallica = 'ride the lightning', 'metallica' , 1984

#print(metallica)
#print(metallica[0])
#print(metallica[1])
#print(metallica[2]) #already you know like strings tuple is also immutable 

#metallica2 = list(metallica)
#print(metallica)      #by this way metallica2 becomes a list by using metallica tuple by turing it into list we can change it becomes mutable

#metallica2[0] = 'master of puppets'
#print(metallica2)  


title ,  artist , year = metallica
print(title)
print(artist)
print(year)

table = ('coffee table',200 , 100 ,75 ,34.50)
print(table[1] * table[2])

name , length , width , hieght , price = table
print(length*width)
