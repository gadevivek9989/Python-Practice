#data structures 
#lists

my_list = [1,2,3,4,5,6]
value = ['vivek','piccac','gundlasagar','velair']

print(value[0])

value[0]='dunna'


value.append('george')
print(value)

#another example of appending in lists

numbers=[]

while True:
    num=int(input("enter an integer,-1 to stop"))
    if num==-1:
        break

    numbers.append(num)

print(numbers)

#example for inserting//

vivek= [2,3,4,6,7]
vivek.insert(2,10)  #(index:number)
print(vivek)
